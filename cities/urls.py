from django.urls import path
from .views import CityListView, CityDetailView, CountryDetailView, CommentViewSet, CommentReplyViewSet, BookingSearchView

comment = CommentViewSet.as_view
reply = CommentReplyViewSet.as_view

urlpatterns = [
    path('cities/',                  CityListView.as_view(),   name='city-list'),
    path('cities/<slug:slug>/',      CityDetailView.as_view(), name='city-detail'),

    path('countries/<slug:slug>/',   CountryDetailView.as_view(), name='country-detail'),

    # Comments — list+create on collection, destroy on instance
    path('cities/<slug:slug>/comments/',
         comment({'get': 'list', 'post': 'create'}),           name='city-comments'),
    path('cities/<slug:slug>/comments/<int:pk>/',
         comment({'delete': 'destroy'}),                        name='comment-destroy'),

    # Replies — create on collection, destroy on instance
    path('cities/<slug:slug>/comments/<int:pk>/replies/',
         reply({'post': 'create'}),                             name='comment-replies'),
    path('cities/<slug:slug>/comments/<int:pk>/replies/<int:reply_pk>/',
         reply({'delete': 'destroy'}),                          name='comment-reply-destroy'),

    path('booking/search/',          BookingSearchView.as_view(), name='booking-search'),
]
