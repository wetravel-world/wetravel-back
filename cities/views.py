import requests
from django.conf import settings
from django.db.models import Avg, Count, F, Q, Sum
from django.utils.text import slugify
from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import City, Comment, CommentReply, CountryImage
from .serializers import (
    CityDetailSerializer,
    CityListSerializer,
    CommentReplySerializer,
    CommentSerializer,
)


BASE_WEIGHT = 10  # base_score counts as this many user votes

def _recalculate_city_score(city_pk):
    try:
        city = City.objects.get(pk=city_pk)
    except City.DoesNotExist:
        return
    approved = Comment.objects.filter(city_id=city_pk, is_approved=True)
    agg = approved.aggregate(total=Sum('score'), count=Count('id'))
    user_sum = agg['total'] or 0
    user_count = agg['count'] or 0
    blended = (float(city.base_score) * BASE_WEIGHT + user_sum) / (BASE_WEIGHT + user_count)
    City.objects.filter(pk=city_pk).update(
        welcome_score=round(blended, 1),
        score_count=user_count,
    )


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


class CountryDetailView(APIView):
    """
    GET /countries/<slug>/ → country overview: average welcome score across its
    cities, a short description, and the list of cities (for a CityCard grid).

    There's no Country model — `country` is a plain field on City — so the slug
    is matched by slugifying each distinct country name.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, slug):
        countries = City.objects.values_list('country', flat=True).distinct()
        country = next((c for c in countries if slugify(c) == slug), None)
        if country is None:
            raise NotFound('Country not found.')

        cities = City.objects.filter(country=country).annotate(
            live_score_count=Count('comments', filter=Q(comments__is_approved=True))
        ).order_by('-welcome_score', 'name')

        average_score = cities.aggregate(avg=Avg('welcome_score'))['avg']
        image = CountryImage.objects.filter(country=country).first()

        # The overview description is a fixed template (not free-form content),
        # so it's localized directly here — no translation tooling needed.
        descriptions = {
            'en': (
                f"Discover how welcoming cities across {country} are for Black travelers, "
                f"African diaspora visitors, and mixed-race couples — based on community "
                f"reviews and welcome scores from real travelers."
            ),
            'fr': (
                f"Découvrez à quel point les villes de {country} sont accueillantes pour les "
                f"voyageurs noirs, les membres de la diaspora africaine et les couples mixtes — "
                f"sur la base d'avis et de scores d'accueil donnés par de vrais voyageurs."
            ),
        }
        lang = request.query_params.get('lang') or ''

        return Response({
            'country': country,
            'slug': slug,
            'average_score': round(average_score, 1) if average_score is not None else None,
            'city_count': cities.count(),
            'hero_image_url': image.image_url if image else '',
            'hero_image_attribution_name': image.attribution_name if image else '',
            'hero_image_attribution_url': image.attribution_url if image else '',
            'description': descriptions.get(lang, descriptions['en']),
            'cities': CityListSerializer(cities, many=True, context={'request': request}).data,
        })


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

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        if self.action == 'list':
            qs = self.get_queryset()
            author_ids = list(qs.values_list('author_id', flat=True).distinct())
            rows = (
                Comment.objects
                .filter(author_id__in=author_ids, is_approved=True)
                .order_by()
                .values('author_id', slug=F('city__slug'))
                .distinct()
            )
            cache: dict[int, list[str]] = {}
            for row in rows:
                cache.setdefault(row['author_id'], []).append(row['slug'])
            ctx['_stamps_cache'] = cache
        return ctx

    def perform_create(self, serializer):
        city = generics.get_object_or_404(City, slug=self.kwargs['slug'])
        serializer.save(author=self.request.user, city=city)
        _recalculate_city_score(city.pk)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('You can only delete your own comments.')
        city_pk = instance.city_id
        instance.delete()
        _recalculate_city_score(city_pk)


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


class TranslateView(APIView):
    """Proxies on-demand text translation through Google Translate so the API key
    never reaches the frontend (mirrors the affiliate_id server-side pattern)."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        text = (request.data.get('text') or '').strip()
        target = (request.data.get('target') or '').strip()

        if not text or not target:
            return Response({'detail': 'text and target are required'}, status=400)
        if len(text) > 5000:
            return Response({'detail': 'text is too long'}, status=400)

        api_key = settings.GOOGLE_TRANSLATE_API_KEY
        if not api_key:
            return Response({'detail': 'Translation is not configured'}, status=503)

        try:
            resp = requests.post(
                'https://translation.googleapis.com/language/translate/v2',
                params={'key': api_key},
                json={'q': text, 'target': target, 'format': 'text'},
                timeout=8,
            )
            resp.raise_for_status()
            translation = resp.json()['data']['translations'][0]
        except (requests.RequestException, KeyError, IndexError, ValueError):
            return Response({'detail': 'Translation failed'}, status=502)

        return Response({
            'translated_text': translation['translatedText'],
            'detected_source_language': translation.get('detectedSourceLanguage', ''),
            'target': target,
        })
