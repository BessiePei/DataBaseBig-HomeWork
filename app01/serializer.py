import re

from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from app01.activities.serializer import ActivitySerializer
from app01.blogs.serializer import BlogSerializer
from app01.dishes.serializer import DishesSerializer
from app01.models import *


# 访客模式
class VisitorSerializer(serializers.ModelSerializer):
    pass


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email']


class UserUpdateSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(read_only=True, error_messages={
    #     "required": "请输入用户名",
    #     "blank": "用户名不能为空"
    # })
    # todo
    user_ab = UserModelSerializer(required=False)

    class Meta:
        model = MyUser
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    isMerchant = serializers.SerializerMethodField()

    id = serializers.SerializerMethodField()
    # username = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'isMerchant']

    def get_id(self, instance):
        info = MyUser.objects.filter(user_ab_id=instance.id)
        if info.exists():
            return info[0].id
        else:
            return Merchant.objects.get(user_ab_id=instance.id).merchantId

    def get_isMerchant(self, instance):
        info = MyUser.objects.filter(user_ab_id=instance.id)

        if info.exists():
            return False
        return True


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

    # def get_userActivities(self, instance):
    #     return instance.userPortrait.url if instance.userPortrait else None
    userFavoriteBlogs = BlogSerializer(many=True)
    userFavoriteMerchants = MerchantSerializer(many=True)
    userActivities = ActivitySerializer(many=True)
    userFavoriteDishes = DishesSerializer(many=True)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'
