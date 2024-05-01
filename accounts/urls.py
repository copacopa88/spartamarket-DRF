from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("<str:username>/", ProfileView.as_view()),
]
