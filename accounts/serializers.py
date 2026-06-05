import requests as http_requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import EmailVerificationToken

User = get_user_model()


# ---------------------------------------------------------------------------
# Shared helper
# ---------------------------------------------------------------------------

def _send_verification_email(user):
    token_obj = EmailVerificationToken.create_for_user(user)
    verify_url = f"{settings.FRONTEND_URL}/auth/verify-email?token={token_obj.token}"
    html = render_to_string('email/verify_email.html', {
        'username': user.username,
        'verify_url': verify_url,
        'frontend_url': settings.FRONTEND_URL,
    })
    send_mail(
        subject='Confirm your WeTravel email',
        message=f"Hi {user.username},\n\nVerify your email: {verify_url}\n\nThis link expires in 24 hours.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html,
        fail_silently=False,
    )


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

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
        user = User.objects.create_user(**validated_data)
        _send_verification_email(user)
        return user


# ---------------------------------------------------------------------------
# Login (email + password → JWT)
# ---------------------------------------------------------------------------

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Accepts email instead of username; blocks unverified accounts."""

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

        data = super().validate(attrs)

        if not self.user.email_verified:
            raise PermissionDenied({
                'detail': 'Please verify your email before logging in.',
                'code': 'email_not_verified',
            })

        return data


# ---------------------------------------------------------------------------
# Email verification
# ---------------------------------------------------------------------------

class VerifyEmailSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, value):
        try:
            token_obj = (
                EmailVerificationToken.objects
                .select_related('user')
                .get(token=value)
            )
        except EmailVerificationToken.DoesNotExist:
            raise serializers.ValidationError('Invalid or already used verification link.')

        if token_obj.is_expired():
            token_obj.delete()
            raise serializers.ValidationError('This verification link has expired. Request a new one.')

        self._token_obj = token_obj
        return value

    def save(self):
        token_obj = self._token_obj
        user = token_obj.user
        user.email_verified = True
        user.save(update_fields=['email_verified'])
        token_obj.delete()
        return user


# ---------------------------------------------------------------------------
# Resend verification email
# ---------------------------------------------------------------------------

class ResendVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email__iexact=value)
        except User.DoesNotExist:
            # Store None — we'll send the same response to avoid user enumeration
            self._user = None
            return value

        if user.email_verified:
            raise serializers.ValidationError('This email address is already verified.')

        self._user = user
        return value

    def save(self):
        if self._user:
            _send_verification_email(self._user)


# ---------------------------------------------------------------------------
# Google OAuth
# ---------------------------------------------------------------------------

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

        self._google_info = info
        return value

    def get_or_create_user(self):
        info = self._google_info
        email = info['email']
        avatar_url = info.get('picture', '')
        base_username = email.split('@')[0]

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'username': _unique_username(base_username),
                'is_google_auth': True,
                'avatar_url': avatar_url,
                'first_name': info.get('given_name', ''),
                'last_name': info.get('family_name', ''),
                'email_verified': True,
            },
        )

        update_fields = []
        if not created and avatar_url and not user.avatar_url:
            user.avatar_url = avatar_url
            update_fields.append('avatar_url')
        if not user.email_verified:
            user.email_verified = True
            update_fields.append('email_verified')
        if update_fields:
            user.save(update_fields=update_fields)

        return user


def _unique_username(base: str) -> str:
    username = base
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1
    return username
