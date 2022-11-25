# -*- codeing = utf-8 -*-
# @Time : 2022/11/21 22:36
# @Author : llcc
# @File : serializer.py
# @Software : PyCharm
from rest_framework import serializers

from app01.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
