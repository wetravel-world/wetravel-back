from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import UserSerializer
from wetravel_back.utils import set_jwt_cookies
from .serializers import EmailTokenObtainPairSerializer, GoogleAuthSerializer, RegisterSerializer

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
    Validation and user lookup are handled by GoogleAuthSerializer.
    """
    serializer_class = GoogleAuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.get_or_create_user()
        refresh = RefreshToken.for_user(user)
        response = Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        set_jwt_cookies(response, refresh.access_token, refresh)
        return response


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
