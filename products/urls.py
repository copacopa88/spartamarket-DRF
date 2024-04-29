from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProductListAPIView.as_view()),
    path("api/products/<int:productId>", views.ProductDetailAPIView.as_view()),
    path("api/products/<int:productId>", views.ProductDetailAPIView.as_view())
]