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

from app01.blogs.serializer import BlogSerializer
from app01.comments.serializer import BlogCommentSerializer
from app01.models import Blog, MyUser, Merchant, BlogComment

from rest_framework import viewsets, status

from app01.mypage import MyPage
from app01.permissions import IsNotAuthenticated
from app01.serializer import UserSerializer


class BlogViewSet(ViewSet):

    def get_all_items(self, request):

        items = Blog.objects.all()
        bs = BlogSerializer(instance=items, many=True)
        return Response(bs.data)

    def add_item(self, request):

        blog = Blog.objects.create(user_ab=request.user)

        item = BlogSerializer(instance=blog, data=request.data, partial=True)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            print(item.errors)
            return Response(item.errors)

    def get_one_item(self, request, pk):
        print(request, pk)
        item = Blog.objects.get(blogId=pk)
        bs = BlogSerializer(instance=item)
        print(bs.data)
        return Response(bs.data)

    def getBlogRemark(self, request, pk):
        items = BlogComment.objects.filter(blog_id=pk)
        ser = BlogCommentSerializer(items, many=True)
        return Response(ser.data)

    def postBlogRemark(self, request, pk):
        blogComment = BlogComment.objects.create(commenter=request.user, blog_id=pk)
        item = BlogCommentSerializer(instance=blogComment, data=request.data, partial=True)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            print(item.errors)
            return Response(item.errors)

    def favoriteBlog(self, request, pk):
        user = MyUser.objects.get(user_ab=request.user)
        user.userFavoriteBlogs.add(pk)
        # print(user.userFavoriteBlogs.all().first().blogId)
        user.save()
        blog = Blog.objects.get(blogId=pk)
        blog.blogFavoriterCnt += 1
        blog.save()
        ser = UserSerializer(user)

        return Response(ser.data)

    def edit_item(self, request, pk):
        instance = Blog.objects.get(blogId=pk)
        bs = BlogSerializer(instance=instance, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self, request, pk):
        Blog.objects.get(blogId=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
