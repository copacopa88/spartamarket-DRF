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
from rest_framework.decorators import permission_classes


@extend_schema(
        tags=["Product"],
        description="Product 목록 조회를 위한 API",
    )
class ProductListAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "인증이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    

class ProductDetailAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    lookup_field = 'productId'
    
    def get_object(self, productId):
        return get_object_or_404(Product, id=productId)
    
    def get(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, productId):
        product = self.get_object(productId)
        if product.user != request.user:
            return Response({"error": "작성자만 삭제할 수 있습니다."}, status=status.HTTP_403_FORBIDDEN)
        product.delete()
        data = {"delete": f"Product({productId}) is deleted."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
