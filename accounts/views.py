# users/views.py
from .models import User
from rest_framework import generics, status
from .serializers import RegisterSerializer
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    

