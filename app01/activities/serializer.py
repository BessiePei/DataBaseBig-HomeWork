from rest_framework import serializers
from app01.models import Activity, ActivitySlide, UserModel, Merchant


class ActivitySerializer(serializers.ModelSerializer):
    # activityOraganizerName 和 activityOrganizerId
    activityOrganizerName = serializers.SerializerMethodField()
    activityOrganizerId = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'

    def get_activityOrganizerName(self, instance):
        merchant = Merchant.objects.get(user_ab_id=instance.user_ab_id)
        return merchant.merchantName

    def get_activityOrganizerId(self, instance):
        merchant = Merchant.objects.get(user_ab_id=instance.user_ab_id)
        return merchant.merchantId


class ActivitySlideSerializer(serializers.ModelSerializer):
    # activityOraganizerName 和 activityOrganizerId
    activityOrganizerName = serializers.SerializerMethodField()
    activityOrganizerId = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'

    def get_activityOrganizerName(self, instance):
        merchant = Merchant.objects.get(user_ab_id=instance.user_ab_id)
        return merchant.merchantName

    def get_activityOrganizerId(self, instance):
        merchant = Merchant.objects.get(user_ab_id=instance.user_ab_id)
        return merchant.merchantId
