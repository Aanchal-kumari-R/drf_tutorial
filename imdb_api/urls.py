from django.urls import path  , include
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns 
from rest_framework.routers import DefaultRouter


# Create a router and register our ViewSets with it.
router = DefaultRouter()  
router.register(r'stream', views.StreamPlatformViewSet, basename='streamplatform')
router.register(r'list', views.WatchListViewSet, basename='watchlist')


urlpatterns = [ 
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('', views.api_root), 
    path('list/<int:pk>/review/',views.ReviewListView.as_view(),name='review-list'),
    path('list/<int:pk>/review-create/',views.ReviewCreate.as_view(),name='review-create'),
    path('list/review/<int:pk>/',views.ReviewDetailView.as_view(),name='review-detail'),
    path('', views.api_root),

]
#urlpatterns = format_suffix_patterns(urlpatterns)
