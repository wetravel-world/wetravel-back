import requests as http_requests
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import UserSerializer
from wetravel_back.utils import set_jwt_cookies
from .serializers import EmailTokenObtainPairSerializer, RegisterSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response = Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        set_jwt_cookies(response, refresh.access_token, refresh)
        return response


class CookieTokenObtainPairView(TokenObtainPairView):
    """Native simplejwt TokenObtainPairView extended to set httpOnly cookies."""
    serializer_class = EmailTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            set_jwt_cookies(response, response.data['access'], response.data['refresh'])
            response.data = {'detail': 'Logged in.'}
        return response


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = Response({'detail': 'Logged out.'})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response


class GoogleAuthView(generics.GenericAPIView):
    """
    Accepts a Google ID token from the frontend (Google Identity Services).
    Verifies it against Google's tokeninfo endpoint, then creates or retrieves
    the user and returns JWT cookies — same pattern as email/password login.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        id_token = request.data.get('id_token')
        if not id_token:
            return Response({'detail': 'id_token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify the token with Google
        try:
            resp = http_requests.get(
                'https://oauth2.googleapis.com/tokeninfo',
                params={'id_token': id_token},
                timeout=5,
            )
            if resp.status_code != 200:
                return Response({'detail': 'Invalid Google token.'}, status=status.HTTP_400_BAD_REQUEST)
            info = resp.json()
        except http_requests.RequestException:
            return Response({'detail': 'Could not verify Google token.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Make sure the token was issued for our app
        # aud can be a string or a comma-separated list
        aud = info.get('aud', '')
        if settings.GOOGLE_CLIENT_ID not in aud:
            return Response({'detail': 'Token audience mismatch.'}, status=status.HTTP_400_BAD_REQUEST)

        email = info.get('email')
        # email_verified is returned as the string "true" by tokeninfo
        if not email or str(info.get('email_verified', '')).lower() != 'true':
            return Response({'detail': 'Google account email is not verified.'}, status=status.HTTP_400_BAD_REQUEST)

        avatar_url = info.get('picture', '')
        given_name = info.get('given_name', '')
        family_name = info.get('family_name', '')

        # Build a username from the email if needed
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

        if not created:
            # Keep avatar up to date
            if avatar_url and not user.avatar_url:
                user.avatar_url = avatar_url
                user.save(update_fields=['avatar_url'])

        refresh = RefreshToken.for_user(user)
        response = Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        set_jwt_cookies(response, refresh.access_token, refresh)
        return response


def _unique_username(base: str) -> str:
    """Return base username, appending a counter if it already exists."""
    username = base
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f'{base}{counter}'
        counter += 1
    return username


class GoogleRedirectView(generics.GenericAPIView):
    """
    Fallback for browsers that block One Tap (Firefox ETP, Safari ITP).
    Redirects to Google's OAuth consent screen via allauth.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        from django.shortcuts import redirect
        from allauth.socialaccount.providers.google.views import oauth2_login
        return oauth2_login(request)


class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token:
            request.data['refresh'] = refresh_token
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            from django.conf import settings
            response.set_cookie(
                'access_token', response.data.get('access'),
                max_age=15 * 60,
                httponly=True,
                secure=not settings.DEBUG,
                samesite='Lax',
            )
            response.data = {'detail': 'Token refreshed.'}
        return response
