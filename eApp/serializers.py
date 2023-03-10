from rest_framework import serializers
from eApp.models import Product, Order, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['items', 'address', 'city', 'phoneNumber', 'totalPrice', 'status'] 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'icon']