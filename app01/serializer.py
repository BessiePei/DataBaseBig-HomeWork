import re

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app01.models import *


class CanteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canteen
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    # userName = serializers.CharField(max_length=30, default='null')
    # userPassword = serializers.CharField(max_length=25, default='123456')
    # userEmail = serializers.CharField(max_length=30, default='')

    class Meta:
        model = User
        fields = ("username", "password", "email")
        # fields = ("userName", "userPassword", "userEmail")
        extra_kwargs = {"password": {"write_only": True},
                        "email": {"required": True}}

    def validate_username(self, username):
        if User.objects.filter(username=username).count():
            raise serializers.ValidationError('用户名已经存在，请查询')
        return username

    # def validate_password(self, attrs):
    #     attrs['password'] = make_password(attrs['password'])
    #     # password_validation.validate_password(attrs)
    #     return attrs

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data["password"])
        user.save()
        return user
