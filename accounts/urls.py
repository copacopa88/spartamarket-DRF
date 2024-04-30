from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", RegisterView.as_view(), name="token_obtain_pair"),
    path("login/", TokenObtainPairView.as_view()),
]
