from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import UserSerializer
from wetravel_back.utils import set_jwt_cookies
from .models import EmailVerificationToken
from .serializers import EmailTokenObtainPairSerializer, GoogleAuthSerializer, RegisterSerializer

User = get_user_model()


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


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _send_verification_email(user)
        return Response(
            {'detail': 'Account created. Check your email to verify your address.'},
            status=status.HTTP_201_CREATED,
        )


class VerifyEmailView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        token_value = request.query_params.get('token', '')
        if not token_value:
            return Response({'detail': 'Missing token.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token_obj = EmailVerificationToken.objects.select_related('user').get(token=token_value)
        except EmailVerificationToken.DoesNotExist:
            return Response({'detail': 'Invalid or already used verification link.'}, status=status.HTTP_400_BAD_REQUEST)

        if token_obj.is_expired():
            token_obj.delete()
            return Response({'detail': 'This verification link has expired. Request a new one.'}, status=status.HTTP_400_BAD_REQUEST)

        user = token_obj.user
        user.email_verified = True
        user.save(update_fields=['email_verified'])
        token_obj.delete()

        refresh = RefreshToken.for_user(user)
        response = Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        set_jwt_cookies(response, refresh.access_token, refresh)
        return response


class ResendVerificationEmailView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', '').strip().lower()
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            # Return 200 to avoid user enumeration
            return Response({'detail': 'If that address is registered and unverified, a new email is on its way.'})

        if user.email_verified:
            return Response({'detail': 'This email is already verified.'}, status=status.HTTP_400_BAD_REQUEST)

        _send_verification_email(user)
        return Response({'detail': 'If that address is registered and unverified, a new email is on its way.'})


class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # Block unverified users before setting cookies
            email = request.data.get('email', '')
            try:
                user = User.objects.get(email__iexact=email)
                if not user.email_verified:
                    return Response(
                        {'detail': 'Please verify your email before logging in.', 'code': 'email_not_verified'},
                        status=status.HTTP_403_FORBIDDEN,
                    )
            except User.DoesNotExist:
                pass
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
        # Google-authenticated users are considered verified
        if not user.email_verified:
            user.email_verified = True
            user.save(update_fields=['email_verified'])
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
            response.set_cookie(
                'access_token', response.data.get('access'),
                max_age=15 * 60,
                httponly=True,
                secure=not settings.DEBUG,
                samesite='Lax',
            )
            response.data = {'detail': 'Token refreshed.'}
        return response
