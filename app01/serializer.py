import re

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app01.models import *


# 访客模式
class VisitorSerializer(serializers.ModelSerializer):
    pass


class UserUpdateSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(read_only=True, error_messages={
    #     "required": "请输入用户名",
    #     "blank": "用户名不能为空"
    # })

    class Meta:
        model = MyUser
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
        # exclude = ['merchantActivityId']
        extra_kwargs = {"merchantId": {"read_only": True}}


class MerchantRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        exclude = ['merchantActivities']


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("password",)
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password"))
        instance.save()
        return instance


# class ModelUserIdSerializer(serializers.ModelSerializer):


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", "password", "email")
        extra_kwargs = {"password": {"write_only": True},
                        "email": {"required": True}}

    # def validate_username(self, username):
    #     if AbstractUser.objects.filter(username=username).count():
    #         raise serializers.ValidationError('用户名已经存在，请查询')
    #     return username
    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        user = UserModel.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    # user_ab = RegistrationSerializer(required=False, read_only=True)
    # user_password = serializers.SerializerMethodField(read_only=True)
    # user_email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MyUser
        fields = '__all__'
        # exclude = ["userFavoriteMerchantId", "userFavoriteDishId", "userActivityId"]

    # def get_user_password(self, instance):
    #     return instance.user_ab.password


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'