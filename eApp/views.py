from django.shortcuts import render
from rest_framework import viewsets, status
from eApp.models import Product, Order
from eApp.serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response

# Create your views here.
class ProductViewset(viewsets.Viewset):
    def list(self, request):
        queryset = Product.objects.all()

        serialized_data = ProductSerializer(queryset, many=True)

        # return data / response
        if not serialized_data.data:
            return Response(
                {'detail': [], 'code':404},
                status=status.HTTP_200_OK
            )
        
        return Response(
            {'detail': serialized_data.data, 'code':200},
            status=status.HTTP_200_OK
        )