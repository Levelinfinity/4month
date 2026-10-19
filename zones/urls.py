from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZoneViewSet, VisitorsViewSet

router = DefaultRouter()
router.register(r'zones', ZoneViewSet, basename='zone')
router.register(r'visitors', VisitorsViewSet, basename='visitor')

urlpatterns = [
    path('', include(router.urls)),
]