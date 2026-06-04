from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import MeViewSet

router = SimpleRouter()
router.register('me', MeViewSet, basename='me')

urlpatterns = [
    path('me/', MeViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}), name='users-me'),
    *router.urls,
]
