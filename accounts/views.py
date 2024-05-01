# users/views.py
from .models import User
from rest_framework import generics, status
from .serializers import RegisterSerializer,ProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .permissions import CustomReadOnly


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.filter(username=['username'])
    permission_classes = [CustomReadOnly]
