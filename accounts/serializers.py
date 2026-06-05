import requests as http_requests
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError('A user with that username already exists.')
        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('A user with that email already exists.')
        return value

    def validate_password(self, value):
        if not any(c.isupper() for c in value):
            raise serializers.ValidationError('Password must contain at least one uppercase letter.')
        if not any(c.isdigit() for c in value):
            raise serializers.ValidationError('Password must contain at least one number.')
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class GoogleAuthSerializer(serializers.Serializer):
    id_token = serializers.CharField()

    def validate_id_token(self, value):
        try:
            resp = http_requests.get(
                'https://oauth2.googleapis.com/tokeninfo',
                params={'id_token': value},
                timeout=5,
            )
        except http_requests.RequestException:
            raise serializers.ValidationError('Could not reach Google to verify the token.')

        if resp.status_code != 200:
            raise serializers.ValidationError('Invalid Google token.')

        info = resp.json()

        aud = info.get('aud', '')
        if settings.GOOGLE_CLIENT_ID not in aud:
            raise serializers.ValidationError('Token was not issued for this application.')

        if str(info.get('email_verified', '')).lower() != 'true':
            raise serializers.ValidationError('Google account email is not verified.')

        if not info.get('email'):
            raise serializers.ValidationError('Google token does not contain an email address.')

        # Attach the parsed info so the view can use it without re-fetching
        self._google_info = info
        return value

    def get_or_create_user(self):
        """Create or retrieve the user from the validated Google token info."""
        info = self._google_info
        email = info['email']
        avatar_url = info.get('picture', '')
        given_name = info.get('given_name', '')
        family_name = info.get('family_name', '')
        base_username = email.split('@')[0]

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'username': _unique_username(base_username),
                'is_google_auth': True,
                'avatar_url': avatar_url,
                'first_name': given_name,
                'last_name': family_name,
            },
        )

        if not created and avatar_url and not user.avatar_url:
            user.avatar_url = avatar_url
            user.save(update_fields=['avatar_url'])

        return user


def _unique_username(base: str) -> str:
    username = base
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1
    return username


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Accepts email instead of username for the JWT login endpoint."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField()
        self.fields.pop(self.username_field, None)

    def validate(self, attrs):
        email = attrs.get('email', '')
        try:
            user_obj = User.objects.get(email__iexact=email)
            attrs[self.username_field] = user_obj.username
        except User.DoesNotExist:
            attrs[self.username_field] = ''
        attrs.pop('email', None)
        return super().validate(attrs)
