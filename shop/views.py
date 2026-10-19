from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Shop
from .serializer import ShopSer
from .pagination import ShopPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ShopViewSets(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSer
    pagination_class = ShopPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['name', 'color']

    search_fields = ['name', 'color']

    ordering_fields = ['name',]

    ordering = ['id',]