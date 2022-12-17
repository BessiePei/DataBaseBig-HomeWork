from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from rest_framework import viewsets, status

from app01.activities.serializer import ActivitySerializer
from app01.dishes.serializer import DishesSerializer
from app01.merchants.serializer import MerchantSerializer, CanteenSerializer, MerchantActivitiesSerializer
from app01.models import Merchant, Canteen, Activity, Dish
from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated
from app01.serializer import RegistrationSerializer


class MerchantModelViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class MerchantViewSet(ViewSet):

    def getHotMerchants(self, request):
        # todo hot merchants
        items = Merchant.objects.all().order_by('merchantFollowerCnt')[:10]
        bs = MerchantSerializer(instance=items, many=True)
        return Response(bs.data)

    def get_one_item(self, request, pk):
        print(request, pk)
        item = Merchant.objects.get(merchantId=pk)
        bs = MerchantSerializer(instance=item)
        return Response(bs.data)

    def getMerchantActivities(self, request, pk):
        merchant = Merchant.objects.get(merchantId=pk)
        activities = merchant.merchantActivities.all()
        # print(activities)
        ser = MerchantActivitiesSerializer(merchant)
        # print(activities)
        # activities = Activity.objects.filter(merchant__merchantId=pk)
        # print(activities)
        return Response(ser.data)

    def getMerchantDishes(self, request, pk):
        merchant = Merchant.objects.get(merchantId=pk)
        # print(merchant)
        dishes = Dish.objects.filter(user_ab_id=merchant.user_ab_id)
        ser = DishesSerializer(dishes, many=True)

        return Response(ser.data)

    def deleteMerchantActivity(self, request, pk):
        # todo 返回信息？
        merchant = Merchant.objects.get(user_ab=request.user)
        activity = Activity.objects.get(activityId=pk)
        if activity.launcher == request.user:
            activity.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={"detail:": "wrong delete"})

    def deleteMerchantDish(self, request, pk):
        # todo 返回信息？
        # check 外联
        dish = Dish.objects.get(dishId=pk)
        print(dish.user_ab, request.user)
        if dish.user_ab == request.user:
            dish.delete()
            ser = DishesSerializer(dish)
            return Response(data=ser.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={"detail:": "wrong delete"})

    def postDish(self, request):
        print(request.data)
        dish = Dish.objects.create(user_ab=request.user, dishPrice=request.data["dishPrice"])
        item = DishesSerializer(instance=dish, data=request.data, partial=True)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            print(item.errors)
            return Response(item.errors)

    def postActivity(self, request):
        print(request.data)
        activity = Activity.objects.create(user_ab=request.user,
                                           activityName=request.data["activityName"],
                                           activityBrief=request.data["activityBrief"],
                                           activityContent=request.data["activityContent"],
                                           # activityBegin=request.data["activityBegin"],
                                           # activityEnd=request.data["activityEnd"]    todo add back
                                           )
        activity.save()
        merchant = Merchant.objects.get(user_ab=request.user)
        merchant.merchantActivities.add(activity.activityId)
        item = ActivitySerializer(activity, data=request.data,partial=True)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            print(item.errors)
            return Response(item.errors)

    # def get_all_items(self, request):
    #
    #     books = Merchant.objects.all()
    #     bs = MerchantSerializer(instance=books, many=True)
    #     return Response(bs.data)
    #
    # def add_item(self, request):
    #     bs = MerchantSerializer(data=request.data)
    #     if bs.is_valid():
    #         bs.save()
    #         return Response(bs.data)
    #     else:
    #         return Response(bs.errors)
    #
    # def get_one_item(self, request, pk):
    #     print(request, pk)
    #     book = Merchant.objects.get(merchantId=pk)
    #     bs = MerchantSerializer(instance=book)
    #     return Response(bs.data)
    #
    # def edit_item(self, request, pk):
    #     instance = Merchant.objects.get(merchantId=pk)
    #     bs = MerchantSerializer(instance=instance, data=request.data)
    #     if bs.is_valid():
    #         bs.save()
    #         return Response(bs.data)
    #     else:
    #         return Response(bs.errors)
    #
    # def delete(self, request, pk):
    #     Merchant.objects.get(merchantId=pk).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CanteenViewSet(ViewSet):

    def get_all_items(self, request):

        items = Canteen.objects.all()
        bs = CanteenSerializer(instance=items, many=True)
        return Response(bs.data)

    def add_item(self, request):
        bs = CanteenSerializer(data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def get_one_item(self, request, pk):
        print(request, pk)
        book = Canteen.objects.get(canteenId=pk)
        bs = CanteenSerializer(instance=book)
        return Response(bs.data)

    def edit_item(self, request, pk):
        instance = Canteen.objects.get(canteenId=pk)
        bs = CanteenSerializer(instance=instance, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, pk):
        Canteen.objects.get(canteenId=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
