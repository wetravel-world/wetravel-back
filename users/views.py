from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cities.models import City, Comment, CommentReply
from cities.serializers import CityListSerializer
from users.serializers import UpdatePasswordSerializer, UpdateProfileSerializer, UserSerializer


class MeViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return UpdateProfileSerializer
        if self.action == 'password':
            return UpdatePasswordSerializer
        return UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response(UserSerializer(request.user).data)

    def partial_update(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(request.user).data)

    @action(detail=False, methods=['post'])
    def password(self, request, *args, **kwargs):
        serializer = UpdatePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Password updated successfully.'})

    @action(detail=False, methods=['get'])
    def activity(self, request, *args, **kwargs):
        user = request.user
        comment_count = Comment.objects.filter(author=user, is_approved=True).count()
        reply_count = CommentReply.objects.filter(author=user, is_approved=True).count()
        city_ids = (
            set(Comment.objects.filter(author=user, is_approved=True).values_list('city_id', flat=True))
            | set(CommentReply.objects.filter(author=user, is_approved=True).values_list('comment__city_id', flat=True))
        )
        cities = City.objects.filter(pk__in=city_ids)
        return Response({
            'comment_count': comment_count,
            'reply_count': reply_count,
            'commented_cities': CityListSerializer(cities, many=True).data,
        })
