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
from app01.comments.serializer import ActivityCommentSerializer, MerchantActivityCommentSerializer
from app01.models import Activity, ActivitySlide, UserModel, MyUser, Merchant, ActivityComment

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated
from app01.serializer import UserSerializer


class ActivityModelViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    @action(methods=['post'], detail=True, url_path='join')
    def userJoinInActivity(self, request, pk):
        instance = Activity.objects.get(activityId=pk)
        instance.activityPersonCnt += 1
        instance.save()

        user_obj = get_object_or_404(MyUser, user_ab=request.user)
        print(user_obj.user_ab)
        user_obj.userActivities.add(pk)
        user_obj.save()

        ser = UserSerializer(user_obj)
        return Response(data=ser.data)

    @action(methods=['get'], detail=True, url_path='remark')
    def getActivityComments(self, request, pk):
        comments = ActivityComment.objects.filter(activity_id=pk)
        ser_comment = ActivityCommentSerializer(instance=comments, many=True)
        return Response(ser_comment.data)

    @action(methods=['post'], detail=True, url_path='postRemark')
    def postActivityComment(self, request, pk):
        print(request.data)
        comment = ActivityComment.objects.create(commenter=request.user, activity_id=pk)
        comment.save()

        item = ActivityCommentSerializer(instance=comment, data=request.data, partial=True)
        print("yes")
        if item.is_valid():
            item.save()
            print("return")
            return Response(item.data)
        else:
            print(item.errors)
            return Response(item.errors)


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


class ActivitySlideViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('activityBegin')
    serializer_class = ActivitySlideSerializer

# class UserJoinInActivity(APIView):
