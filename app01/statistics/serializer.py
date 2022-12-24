from rest_framework import serializers

from app01.merchants.serializer import MerchantSerializer
from app01.models import Dish, ClassifyUserFavoriteDishes


class ClassifyFavoriteDishesSerializer(serializers.ModelSerializer):
    # merchant = MerchantSerializer()
    value = serializers.ModelSerializer(required=False)
    name = serializers.ModelSerializer(required=False)

    class Meta:
        model = ClassifyUserFavoriteDishes
        fields = '__all__'

    def get_value(self, instance):
        return instance.dishesCnt

    def get_name(self, instance):
        return instance.merchantName
