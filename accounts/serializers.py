from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator # 유니크 값을 찾기 위한 도구
from django.contrib.auth import authenticate


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())], #유저네임(로그인에 쓰일 id) 중복 체크
    )
    name = serializers.CharField(
        write_only=True,
        required=True,
    )
    
    birthday = serializers.DateField(input_formats=["%Y-%m-%d"], required=True)
    
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())], # 이메일 중복 체크
    )
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password], # 기본적인 비밀번호 체크
    )
    password2 = serializers.CharField( # 비밀번호 확인을 위한 필드
        write_only=True,
        required=True,
    )
    
    gender=serializers.CharField(
        required=False,   #성별은 빈칸으로 놔둬도 회원가입이 될수 있도록 models에도 수정을 함
        allow_blank=True
    )
    
    introduce=serializers.CharField(
        required=False, 
        allow_blank=True    #자기소개 역시 마찬가지
    )
    
    profile_photo=serializers.ImageField(
        required=False,   #프로필 사진도 넣어보았다.
    )
    

    class Meta:
        model = User
        fields = ('username','name', 'email', 'password', 'password2', 'birthday', 'gender', 'introduce', 'profile_photo') #입력가능한 목록들

    def validate(self, data): # password과 password2의 일치 여부 확인
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "재입력한 비밀번호가 서로 맞지 않습니다."})
        
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],
            birthday=validated_data['birthday'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            introduce=validated_data['introduce'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "name", "email", "birthday", "gender", "introduce", "profile_photo")
