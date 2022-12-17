from rest_framework import serializers
from app01.models import Activity, ActivitySlide


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ActivitySlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
