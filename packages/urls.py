from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, ReviewViewSet, HotelViewSet, PackageViewSet

router = DefaultRouter()
router.register(r'packages', PackageViewSet)
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'hotels', HotelViewSet, basename='hotel')

urlpatterns = [
    path('api/', include(router.urls)),
]
