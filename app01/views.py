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

from app01.models import *

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated
from app01.serializer import *


class GoodsView(APIView):

    # pagination_class = MyPage
    def get(self, request, *args, **kwargs):
        goods = Canteen.objects.all()
        goods_json = CanteenSerializer(goods, many=True)
        print(goods_json.data)
        return Response(goods_json.data)

    def post(self, request):
        data = request.data
        print(data)
        ser_data = CanteenSerializer(data=request.data)
        if ser_data.is_valid():  # 判断数据合法性
            goods = ser_data.save()  # 保存数据，实际上调用create
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors)

    def put(self, request, *args, **kwargs):
        print(request.data)
        try:
            goods = Canteen.objects.get(id=kwargs.get("id"))
        except Canteen.DoesNotExist:
            raise Http404
        ser_data = CanteenSerializer(instance=goods, data=request.data, context={"request": request})
        if ser_data.is_valid():
            goods = ser_data.save()
            return Response(ser_data.data)
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        goods = Canteen.objects.filter(id=kwargs.get("id"))
        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = MyPage


class RegisterView(APIView):
    permission_classes = (IsNotAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        Token.objects.get_or_create(user=user)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):
    permission_classes = (IsNotAuthenticated,)

    def post(self, request):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username)
        if user is not None:
            user = authenticate(username=username, password=password)
            if user:    # 如果验证通过
                if user.is_active:  # 如果用户状态为激活
                    # print("登录")
                    login(request, user)
            serializer = UserSerializer(user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "登录失败。"}, status.HTTP_401_UNAUTHORIZED)