from rest_framework import serializers

from .models import Shop

class ShopSer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'color', 'logo')

