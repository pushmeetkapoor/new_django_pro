from air_compressors import views

from django.conf.urls import url, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'air_compressors', views.AirCompressorViewSet)

urlpatterns = [
        url(r'^', include(router.urls))
]
