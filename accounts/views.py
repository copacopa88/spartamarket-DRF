# users/views.py
from rest_framework import status
from .models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,ProfileSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
           user = serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        password = request.data.get("password")
        if not password:
            return Response({"error": "password is required"}, status=400)

        if not request.user.check_password(password):
            return Response({"error": "password is incorrect"}, status=400)

        request.user.delete()
        return Response({"회원탈퇴 완료"},status=204)


    

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
