from django.http import JsonResponse, HttpResponse
from .models import Product
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class ProductListAPIView(APIView):
    
    permission_classes = [IsAuthenticated] #로그인 여부
    
    @extend_schema(
        tags=["Product"],
        description="Product 목록 조회를 위한 API",
    )
    
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["Product"],
        description="Product 생성을 위한 API",
        request=ProductSerializer
    )
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ProductDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, product_pk):
        return get_object_or_404(Product, pk=product_pk)
    
    def get(self, request, product_pk):
        product = self.get_object(product_pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, product_pk):
        product = self.get_object(product_pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, product_pk):
        article = self.get_object(product_pk)
        article.delete()
        data = {"delete": f"Product({product_pk}) is deleted."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
