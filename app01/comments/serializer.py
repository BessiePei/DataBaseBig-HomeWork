from django.shortcuts import get_object_or_404
from rest_framework import serializers

from app01.activities.serializer import ActivitySerializer
from app01.merchants.serializer import MerchantSerializer
from app01.models import ActivityComment, BlogComment, DishComment
from app01.serializer import UserSerializer


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'


class DishCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishComment
        fields = '__all__'


class ActivityCommentSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    # user = UserSerializer(required=False)

    class Meta:
        model = ActivityComment
        fields = '__all__'


class MerchantActivityCommentSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    merchant = MerchantSerializer(required=False)

    class Meta:
        model = ActivityComment
        fields = '__all__'

# class ActivitySlideSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ActivitySlide
#         fields = '__all__'
