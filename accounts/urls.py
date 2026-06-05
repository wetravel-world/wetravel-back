from django.urls import path
from .views import (
    RegisterView, CookieTokenObtainPairView, LogoutView, CookieTokenRefreshView,
    GoogleAuthView, GoogleRedirectView, VerifyEmailView, ResendVerificationEmailView,
)

urlpatterns = [
    path('register/',              RegisterView.as_view(),               name='auth-register'),
    path('login/',                 CookieTokenObtainPairView.as_view(),  name='auth-login'),
    path('logout/',                LogoutView.as_view(),                 name='auth-logout'),
    path('token/refresh/',         CookieTokenRefreshView.as_view(),     name='token-refresh'),
    path('google/',                GoogleAuthView.as_view(),             name='auth-google'),
    path('google/redirect/',       GoogleRedirectView.as_view(),         name='auth-google-redirect'),
    path('verify-email/',          VerifyEmailView.as_view(),            name='auth-verify-email'),
    path('resend-verification/',   ResendVerificationEmailView.as_view(), name='auth-resend-verification'),
]
