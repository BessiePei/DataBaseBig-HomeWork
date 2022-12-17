from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from app01.activities.serializer import ActivitySerializer, ActivitySlideSerializer
from app01.comments.serializer import BlogCommentSerializer
from app01.models import Activity, ActivitySlide, UserModel, MyUser, BlogComment

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated


class ActivityModelViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(methods=['post'], detail=True, url_path='join')
    def userJoinInActivity(self, request, pk):
        instance = Activity.objects.filter(activityId=pk).first()
        instance.activityPersonCnt += 1
        instance.save()

        user_obj = get_object_or_404(MyUser, user_ab=request.user)
        print(user_obj)
        user_activities = list(user_obj.userActivityId.all())
        print(user_activities)
        user_activities.append(instance)
        user_obj.userActivityId.clear()
        user_obj.userActivityId.add(*user_activities)
        user_obj.save()
        return Response(data={"detail": "参加成功"})

    @action(methods=['get'], detail=True, url_path='remark')
    def getActivityComments(self, request, pk):
        instance = Activity.objects.filter(activityId=pk).first()

    # get_all_items
    # def list(self, request, *args, **kwargs):

    # add_item
    # def create(self, request, *args, **kwargs):

    # get_one_item
    # def retrieve(self, request, *args, **kwargs):

    # edit_item
    # def update(self, request, *args, **kwargs):

    # delete
    # def destroy(self, request, *args, **kwargs):





class BlogCommentModelViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer


