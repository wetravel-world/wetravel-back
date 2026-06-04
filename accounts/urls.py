from django.urls import path
from .views import RegisterView, CookieTokenObtainPairView, LogoutView, CookieTokenRefreshView

urlpatterns = [
    path('register/',      RegisterView.as_view(),                name='auth-register'),
    path('login/',         CookieTokenObtainPairView.as_view(),   name='auth-login'),
    path('logout/',        LogoutView.as_view(),                  name='auth-logout'),
    path('token/refresh/', CookieTokenRefreshView.as_view(),      name='token-refresh'),
]
