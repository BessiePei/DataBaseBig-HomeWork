from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

# from app01.dishes.models import DishesSlide
from app01.comments.serializer import DishCommentSerializer
from app01.dishes.serializer import DishesSerializer
from app01.models import Dish, DishComment, MyUser

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated
from app01.serializer import UserSerializer
from django.db import connection

from app01.statistics.serializer import ClassifyFavoriteDishesSerializer

cursor = connection.cursor()


def beforeDeleteActivity():
    sql = 'CREATE TRIGGER beforeDeleteActivity before delete ' \
          'ON db_hw.backend_activity FOR EACH ROW BEGIN ' \
          'delete from db_hw.backend_user where backend_user.user_ab_id=OLD.user_ab_id;' \
          'END'

    cursor.execute(sql)


def afterUserFavoriteBlog():
    sql = 'CREATE TRIGGER afterUserFavoriteBlog after update ' \
          'ON db_hw.backend_user FOR EACH ROW begin ' \
          'UPDATE db_hw.backend_blog ' \
          'set blogFavoriterCnt=blogFavoriterCnt+1 ' \
          'where user_ab_id=NEW.user_ab_id;' \
          'end'
    cursor.execute(sql)


class ClassifyDishesViewSet(ViewSet):
    def get_classified(self, request):
        sql = 'SELECT merchantName, count(*) from db_hw.backend_user, db_hw.backend_user_userfavoritedishes, db_hw.backend_dish, db_hw.backend_merchant ' \
              'where backend_user_userfavoritedishes.myuser_id=backend_user.id and ' \
              'backend_user_userfavoritedishes.dish_id=backend_dish.dishId and ' \
              'backend_user.user_ab_id=%s and ' \
              'backend_dish.user_ab_id=backend_merchant.user_ab_id ' \
              'group by backend_dish.user_ab_id'
        print(request.user.id)
        print(type(MyUser.objects.all()))
        cursor.execute(
            sql,
            [request.user.id]
        )
        items = cursor.fetchall()
        print(items)
        liss = []
        default = {"merchantName": "null", "dishesCnt": 0}
        single = {}
        for item in items:
            single["value"] = item[1]
            single["name"] = item[0]
            data = ClassifyFavoriteDishesSerializer(data=single)
            if data.is_valid():
                data.save()
            liss.append(single)
            single = {}
        if len(liss) == 0:
            liss.append(default)
        print(liss)
        return Response(data=liss)
