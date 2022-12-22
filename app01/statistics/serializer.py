from rest_framework import serializers

from app01.merchants.serializer import MerchantSerializer
from app01.models import Dish, ClassifyUserFavoriteDishes



class ClassifyFavoriteDishesSerializer(serializers.ModelSerializer):
    # merchant = MerchantSerializer()
    class Meta:
        model = ClassifyUserFavoriteDishes
        fields = '__all__'
