from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from .models import Zone, Visitors
from .serializers import ZoneSerializer, VisitorsSerializer
from .pagination import ZonePagination

# Create your views here.

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all().order_by('-id')
    serializer_class = ZoneSerializer
    pagination_class = ZonePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['location']
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'name']


class VisitorsViewSet(viewsets.ModelViewSet):
    queryset = Visitors.objects.all().order_by('-id')
    serializer_class = VisitorsSerializer
    pagination_class = ZonePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_allowed', 'zone']
    search_fields = ['full_name', 'info']
    ordering_fields = ['id', 'full_name']