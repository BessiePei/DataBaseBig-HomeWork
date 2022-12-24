from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.dishes.views import DishViewSet, SearchView

router = DefaultRouter()
# router.register('slider', DishesSlideViewSet)

urlpatterns = [
    path("hotdishes/", DishViewSet.as_view({
        "get": "get_all_items",  #
    })),
    path("dish/<int:pk>/", DishViewSet.as_view({
        "get": "get_one_item",  # function getDishByID(id)
    })),
    path("dish/<int:pk>/remark/", DishViewSet.as_view({
        "get": "getDishRemark",  # function getDishByID(id)
        "post": "postDishRemark",  # function getDishByID(id)
    })),
    # path("dish/<int:pk>/remark/", DishViewSet.as_view({
    #     "post": "postDishRemark",  # function getDishByID(id)
    # })),
    path("dish/<int:pk>/favorite/", DishViewSet.as_view({
        "post": "favoriteDish",  # function getDishByID(id)
    })),
    path("dish/", SearchView.as_view({
        "get": "searchDishes",
    })),
]
