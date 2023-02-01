from django.shortcuts import render
from rest_framework import viewsets, status
from eApp.models import Product, Order
from eApp.serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response

# Create your views here.
class ProductViewset(viewsets.ViewSet):
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

    def create(self, request):
        # get data from request payload
        # pass through serializer
        serialized_data = ProductSerializer(data=request.data)

        if not serialized_data.is_valid():
            return Response(
                {'detail': serialized_data.errors, 'code':400},
                status=status.HTTP_400_BAD_REQUEST
            )

        # store data in database
        serialized_data.save()

        # return response
        return Response(
            {'detail': 'Product added succesfully', 'code': 200},
            status=status.HTTP_201_CREATED
        )

    def retrieve(self, request, pk=None):
        try:
            queryset = Product.objects.get(pk=pk)
            serialized_data = ProductSerializer(queryset)
            return Response(
                    {'details':serialized_data.data, 'code':200},
                    status=status.HTTP_200_OK
                )

        except Product.DoesNotExist:
            return Response(
                {'details':'Product Does Not Exist', 'code': 400},
                status=status.HTTP_200_OK
            )

    
    def update(self, request, pk=None):
        serialized_data = ProductSerializer(data=request.data)
        if not serialized_data.is_valid():
                return Response(
                    {'details':serialized_data.errors, 'code': 400},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        product = Product.objects.filter(pk=pk)
            
        if product:
                product.update(**serialized_data.data)
                return Response(
                    {'details':'Product updated', 'code':200},
                    status=status.HTTP_200_OK
                )
        return Response(
                {'details':'Product to be updated does not exist', 'code':400},
                status=status.HTTP_200_OK
            )

    def delete(self, request, pk=None):
        Product.objects.filter(pk=pk).delete()
        return Response(
            {'details':'Succesfully deleted product.', 'code':200},
            status=status.HTTP_200_OK
        )

