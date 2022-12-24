from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.merchants.views import MerchantViewSet, MerchantModelViewSet

router = DefaultRouter()
# router.register('merchant', MerchantModelViewSet)   # getMerChantByID

urlpatterns = [
    path("hotmerchants/", MerchantViewSet.as_view({
        "get": "getHotMerchants",  # function getHotMerChants()
    })),

    path('merchant/<int:pk>/', MerchantViewSet.as_view({
        "get": "get_one_item",  # function getMerChantByID()
    })),
    path('merchant/<int:pk>/activities/', MerchantViewSet.as_view({
        "get": "getMerchantActivities",  # function getMerchantActivities()
    })),
    path('merchant/<int:pk>/dishes/', MerchantViewSet.as_view({
        "get": "getMerchantDishes",  # function getMerchantDishes()
    })),
    path('merchant/1/dishes/<int:pk>/', MerchantViewSet.as_view({
        "delete": "deleteMerchantDish",  # function deleteMerchantDish()
    })),
    path('merchant/1/activity/<int:pk>/', MerchantViewSet.as_view({
        "delete": "deleteMerchantActivity",  # function deleteMerchantDish()
    })),
    path('merchant/dishes/', MerchantViewSet.as_view({
        "post": "postDish",  # function postDish()
    })),
    path('merchant/activities/', MerchantViewSet.as_view({
        "post": "postActivity",  # function postActivity()
    })),

]
