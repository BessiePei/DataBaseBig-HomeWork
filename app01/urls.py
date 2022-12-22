from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.views import *

router = DefaultRouter()
router.register('usersList', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('app01.activities.urls')),
    path('', include('app01.blogs.urls')),
    # path('', include('app01.comments.urls')),
    path('', include('app01.dishes.urls')),
    path('', include('app01.merchants.urls')),
    path('', include('app01.statistics.urls')),
    path('users/', UserRegisterView.as_view()),
    path('merchants/', MerchantRegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path("users/1/", UserView.as_view({
        "get": "get_item",
        "patch": "edit_item",  # function edit_item()
    })),
    path("changePassword/", UserView.as_view(
        {
            "patch": "changePassword",
        }
    )),
    path("feedback/", UserView.as_view({
        "post": "submitFeedBack",
    })),
    path("users/1/dishes/", UserView.as_view({
        "get": "getUserDish",
    })),
    path("users/1/activities/", UserView.as_view({
        "get": "getUserActivity",
    })),
    path("users/1/dishes/<int:pk>/", UserView.as_view({
        "delete": "deleteUserDish",
    })),
    path("users/1/activities/<int:pk>/", UserView.as_view({
        "delete": "deleteUserActivity",
    })),

    path("users/1/blogs/", UserView.as_view({
        "get": "getUserBlog",
    })),
    path("users/1/loveblogs/", UserView.as_view({
        "get": "getUserLoveBlog",
    })),

    path("users/1/loveblogs/<int:pk>/", UserView.as_view({
        "delete": "deleteUserLoveBlog",
    })),
    path("users/1/blogs/<int:pk>/", UserView.as_view({
        "delete": "deleteUserBlog",
    })),
]
