from django.contrib import auth
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from app01.activities.serializer import ActivitySerializer
from app01.blogs.serializer import BlogSerializer
from app01.dishes.serializer import DishesSerializer
from app01.models import *

from rest_framework import viewsets, status

from app01.myfilter import UsersFilter
from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated
from app01.serializer import *

UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    # pagination_class = MyPage
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 指定过滤器的配置类, 配置搜索的项
    # filter_fields = ('username',)  # 过滤字段
    filterset_class = UsersFilter
    # 搜索字段
    search_fields = ('username', 'age')
    # 排序字段
    ordering_fields = ('username', 'id')


class UserView(ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_item(self, request):
        print(request.user.id)
        user = MyUser.objects.get(user_ab_id=request.user.id)
        bs = UserSerializer(instance=user)
        return Response(bs.data)

    # 修改密码的端口另写，接口也改一下
    def edit_item(self, request):
        print(request.user)
        instance = MyUser.objects.get(user_ab=request.user)
        # 用户名 按照 userNickName 传
        bs = UserUpdateSerializer(instance=instance, data=request.data, partial=True)
        if bs.is_valid():
            bs.save()
            return Response(bs.data, status.HTTP_200_OK)
        else:
            return Response(bs.errors, status.HTTP_400_BAD_REQUEST)

    def changePassword(self, request):
        if request.user.check_password(request.data.get("old_password")):
            serializer = ChangePasswordSerializer(request.user, request.data)
            if serializer.is_valid():
                serializer.save()
                # Updating the password logs out all other sessions for the user
                # except the current one.
                update_session_auth_hash(request, request.user)
                print(serializer.data)  # 为空
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "旧密码不正确"}, status.HTTP_400_BAD_REQUEST)

    def getUserDish(self, request):
        user = MyUser.objects.get(user_ab=request.user)
        dishes = user.userFavoriteDishes.all()
        ser = DishesSerializer(dishes, many=True)
        return Response(ser.data)

    def getUserActivity(self, request):
        user = MyUser.objects.get(user_ab=request.user)
        activities = user.userActivities.all()
        ser = ActivitySerializer(activities, many=True)
        return Response(ser.data)

    def deleteUserDish(self, request, pk):
        user = MyUser.objects.get(user_ab=request.user)
        info = user.userFavoriteDishes.remove(pk)
        # todo 返回值？
        return Response(status=status.HTTP_204_NO_CONTENT)

    def deleteUserActivity(self, request, pk):
        user = MyUser.objects.get(user_ab=request.user)
        info = user.userActivities.remove(pk)
        # todo 返回值？
        return Response(status=status.HTTP_204_NO_CONTENT)

    def getUserBlog(self, request):
        blogs = Blog.objects.filter(user_ab=request.user)
        item = BlogSerializer(blogs, many=True)

        return Response(item.data)

    def getUserLoveBlog(self, request):
        user = MyUser.objects.get(user_ab=request.user)
        loveBlogs = user.userFavoriteBlogs.all()
        ser = BlogSerializer(loveBlogs, many=True)
        return Response(ser.data)

    def deleteUserBlog(self, request, pk):
        # todo 删除的前置条件?
        Blog.objects.get(blogId=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def deleteUserLoveBlog(self, request, pk):
        user = MyUser.objects.get(user_ab=request.user)
        info = user.userFavoriteBlogs.remove(pk)
        # todo 返回值？
        return Response(status=status.HTTP_204_NO_CONTENT)

    def submitFeedBack(self, request):
        feedback = FeedbackSerializer(data=request.data)
        if feedback.is_valid():
            feedback.save()
            return Response(feedback.data)
        else:
            return Response(feedback.errors)


class MerchantRegisterView(APIView):
    permission_classes = (IsNotAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = RegistrationSerializer(
            data={"username": request.data["merchantName"], "password": request.data["merchantPassword"],
                  "email": "125346@qq.com"})

        if serializer.is_valid():
            print('yes')
            user_ab = serializer.save()
            # merchant = Merchant.objects.create(user_ab=user_ab, isMerchant=True)
            data = {"user_ab": user_ab.id, "merchantName": request.data["merchantName"],
                    "merchantPassword": request.data["merchantPassword"],
                    "merchantAddr": request.data["merchantAddr"],
                    "merchantOpen": request.data["merchantOpen"],
                    "merchantClose": request.data["merchantClose"],
                    "merchantHead": request.data["merchantHead"],
                    "isMerchant": True,
                    "merchantPhone": request.data["merchantPhone"],
                    "merchantPortrait": request.data["merchantPortrait"]}
            merchantSerializer = MerchantRegisterSerializer(data=data)
            if merchantSerializer.is_valid():
                print('merchantSer is valid')
                merchantUser = merchantSerializer.save()
                # merchantUser = Merchant.objects.create(user_ab=user, merchantName=request.data["merchantName"],
                #                                        merchantPassword=request.data["merchantPassword"],
                #                                        merchantAddr=request.data["merchantAddr"],
                #                                        merchantOpen=request.data["merchantOpen"],
                #                                        merchantClose=request.data["merchantClose"],
                #                                        merchantHead=request.data["merchantHead"],
                #                                        merchantPhone=request.data["merchantPhone"],
                #                                        merchantPortrait=request.data["merchantPortrait"])

                user = authenticate(username=request.data.get('merchantName'),
                                    password=request.data.get('merchantPassword'))
                login(request, user)

                return Response(
                    data=merchantSerializer.data,
                    status=status.HTTP_201_CREATED
                )
            else:
                print(merchantSerializer.errors)
                return Response(data=merchantSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(APIView):
    permission_classes = (IsNotAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(type(request.data))
        print(request.data)
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user_ab = serializer.save()
            print(user_ab)
            user = MyUser.objects.create(user_ab=user_ab, username=request.data['username'], isMerchant=False)
            # user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
            # login(request, user)
            serializer = UserSerializer(user)

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )

        else:
            print(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (IsNotAuthenticated,)

    def post(self, request):
        print(request.data)
        user_ab = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user_ab is not None:
            login(request, user_ab)
            print(request.user)
            ser = LoginSerializer(user_ab)
            # user = MyUser.objects.get(user_ab=user_ab)
            # serializer = UserSerializer(user)
            return Response(data=ser.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "登录失败。"}, status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "登出成功"}, status.HTTP_200_OK)
