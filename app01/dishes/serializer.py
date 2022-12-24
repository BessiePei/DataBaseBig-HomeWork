from rest_framework import serializers
from app01.models import Dish, Merchant


class DishesSerializer(serializers.ModelSerializer):
    dishSeller = serializers.SerializerMethodField()
    class Meta:
        model = Dish
        fields = '__all__'
    def get_dishSeller(self, instance):
        dishSeller = Merchant.objects.get(user_ab_id=instance.user_ab_id)
        return dishSeller.merchantName

