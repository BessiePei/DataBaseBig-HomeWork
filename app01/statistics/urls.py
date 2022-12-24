from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.dishes.views import DishViewSet
from app01.statistics.views import ClassifyDishesViewSet

router = DefaultRouter()
# router.register('slider', DishesSlideViewSet)

urlpatterns = [
    path("chart/", ClassifyDishesViewSet.as_view({
        "get": "get_classified",  #
    })),
]
