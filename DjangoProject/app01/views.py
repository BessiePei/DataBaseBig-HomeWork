from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

from app01.models import User

from rest_framework import viewsets

from app01.models import User
from app01.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def add_user(request):
    print(request.POST)
    response = {}
    return JsonResponse(response)
    #
    # return JsonResponse(
    #     {
    #         "factors": factors,
    #         "options": options
    #     }
    # )


def login(request):
    print(request.POST)
    print(request.GET)
    userName = request.POST.get("username2")
    password = request.POST.get("password2")
    return JsonResponse({
        "status": 200
    })
