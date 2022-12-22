from rest_framework import serializers

from app01.activities.serializer import ActivitySerializer
from app01.models import Merchant


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'


class MerchantActivitiesSerializer(serializers.ModelSerializer):
    merchantActivities = ActivitySerializer(many=True)

    class Meta:
        model = Merchant
        # fields = ['merchantActivities']
        fields = '__all__'

