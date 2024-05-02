from django.urls import path
from .views import ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenBlacklistView
)
from . import views

urlpatterns = [
    path("", views.RegisterView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("<str:username>/", ProfileView.as_view(), name="ProfileView"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
]
