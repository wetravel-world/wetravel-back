from django.conf import settings
from django.db.models import Count, Q
from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City, Comment, CommentReply
from .serializers import (
    CityDetailSerializer,
    CityListSerializer,
    CommentReplySerializer,
    CommentSerializer,
)
from .tasks import recalculate_city_score


class CityListView(generics.ListAPIView):
    serializer_class = CityListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = City.objects.annotate(
            live_score_count=Count('comments', filter=Q(comments__is_approved=True))
        )
        q = self.request.query_params.get('q')
        continent = self.request.query_params.get('continent')
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(country__icontains=q) | Q(continent__icontains=q))
        if continent and continent != 'All':
            qs = qs.filter(continent=continent)
        return qs


class CityDetailView(generics.RetrieveAPIView):
    serializer_class = CityDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        return City.objects.annotate(
            live_score_count=Count('comments', filter=Q(comments__is_approved=True))
        )


class CommentViewSet(viewsets.ModelViewSet):
    """
    Exposed actions (via URL mapping):
      GET    /cities/{slug}/comments/       → list
      POST   /cities/{slug}/comments/       → create
      DELETE /cities/{slug}/comments/{pk}/  → destroy
    """
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ('create', 'destroy'):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        return (
            Comment.objects
            .filter(city__slug=self.kwargs['slug'], is_approved=True)
            .prefetch_related('replies', 'replies__author')
            .select_related('author')
        )

    def perform_create(self, serializer):
        city = generics.get_object_or_404(City, slug=self.kwargs['slug'])
        serializer.save(author=self.request.user, city=city)
        recalculate_city_score.delay(city.pk)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('You can only delete your own comments.')
        city_pk = instance.city_id
        instance.delete()
        recalculate_city_score.delay(city_pk)


class CommentReplyViewSet(viewsets.ModelViewSet):
    """
    Exposed actions (via URL mapping):
      POST   /cities/{slug}/comments/{pk}/replies/            → create
      DELETE /cities/{slug}/comments/{pk}/replies/{reply_pk}/ → destroy
    """
    serializer_class = CommentReplySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'reply_pk'

    def get_queryset(self):
        return CommentReply.objects.filter(
            comment__pk=self.kwargs['pk'],
            comment__city__slug=self.kwargs['slug'],
        )

    def perform_create(self, serializer):
        comment = generics.get_object_or_404(
            Comment,
            pk=self.kwargs['pk'],
            city__slug=self.kwargs['slug'],
            is_approved=True,
        )
        serializer.save(author=self.request.user, comment=comment)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('You can only delete your own replies.')
        instance.delete()


class BookingSearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        city_slug = request.query_params.get('city', '')
        checkin = request.query_params.get('checkin', '')
        checkout = request.query_params.get('checkout', '')

        try:
            city = City.objects.get(slug=city_slug)
            city_name = city.name
        except City.DoesNotExist:
            city_name = city_slug.replace('-', ' ').title()

        affiliate_id = settings.BOOKING_AFFILIATE_ID
        url = (
            f'https://www.booking.com/searchresults.html'
            f'?ss={city_name}'
            f'&checkin={checkin}'
            f'&checkout={checkout}'
            f'&aid={affiliate_id}'
            f'&utm_source=wetravel'
            f'&utm_medium=city_page'
            f'&utm_campaign={city_slug}'
        )
        return Response({'booking_url': url, 'city': city_name})
