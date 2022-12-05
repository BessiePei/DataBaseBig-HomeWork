
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.views import *

router = DefaultRouter()
router.register('usersList', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('canteens/', GoodsView.as_view()), # get post
    path('canteens/<int:id>', GoodsView.as_view()), # put delete
    path('', TemplateView.as_view(template_name='index.html'))
]
