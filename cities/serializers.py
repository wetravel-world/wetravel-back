from rest_framework import serializers
from .models import City, Place, Comment, CommentReply


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'place_type', 'image_url', 'address', 'google_place_id')


class CommentReplySerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_avatar_url = serializers.URLField(source='author.avatar_url', read_only=True)

    class Meta:
        model = CommentReply
        fields = ('id', 'author_username', 'author_avatar_url', 'body', 'created_at')
        read_only_fields = ('id', 'author_username', 'author_avatar_url', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_avatar_url = serializers.URLField(source='author.avatar_url', read_only=True)
    author_stamps = serializers.SerializerMethodField()
    replies = CommentReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author_username', 'author_avatar_url', 'author_stamps', 'body', 'score', 'created_at', 'replies')
        read_only_fields = ('id', 'author_username', 'author_avatar_url', 'author_stamps', 'created_at', 'replies')

    def get_author_stamps(self, obj):
        cache = self.context.get('_stamps_cache')
        if cache is not None:
            return cache.get(obj.author_id, [])
        return list(
            Comment.objects.filter(author_id=obj.author_id, is_approved=True)
            .values_list('city__slug', flat=True)
            .distinct()
        )

    def validate_score(self, value):
        if not 1 <= value <= 10:
            raise serializers.ValidationError('Score must be between 1 and 10.')
        return value


class CityListSerializer(serializers.ModelSerializer):
    score_count = serializers.IntegerField(source='live_score_count', read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'continent', 'slug', 'welcome_score', 'score_count', 'hero_image_url', 'description')


class CityDetailSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    score_count = serializers.IntegerField(source='live_score_count', read_only=True)

    class Meta:
        model = City
        fields = (
            'id', 'name', 'country', 'continent', 'slug', 'description',
            'welcome_score', 'score_count', 'latitude', 'longitude',
            'hero_image_url', 'meta_description', 'places', 'created_at',
        )
