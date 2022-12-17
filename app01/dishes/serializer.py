from rest_framework import serializers
from app01.models import Dish


class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'



