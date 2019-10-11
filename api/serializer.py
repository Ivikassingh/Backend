from rest_framework import serializers
from .models import Orders,Locations,Restaurant,FoodList

class OrdersFoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Orders

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Locations
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Restaurant
class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FoodList