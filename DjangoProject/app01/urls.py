# -*- codeing = utf-8 -*-
# @Time : 2022/11/21 17:55
# @Author : llcc
# @File : urls.py.py
# @Software : PyCharm

from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.views import *

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', add_user),
    # path('users/1/', getUserByID),
    path('login/', login),
    path('', TemplateView.as_view(template_name='index.html'))
]
