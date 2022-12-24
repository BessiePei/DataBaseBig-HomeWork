from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.blogs.views import BlogViewSet

router = DefaultRouter()
# router.register('blog', BlogModelViewSet)

urlpatterns = [
    path("visitorblogs/", BlogViewSet.as_view({
        "get": "get_all_items",  # function getSlide()
    })),
    path("blog/", BlogViewSet.as_view({
        "post": "add_item"  # sendBlog
    })),
    path("blog/<int:pk>/", BlogViewSet.as_view({
        "get": "get_one_item",  # function getBlogById(id)  # 发帖人 blogPostName
        # "put": "edit_item",
        # "delete": "delete",
    })),
    path("blog/<int:pk>/remark/", BlogViewSet.as_view({
        "get": "getBlogRemark",  # function getBlogRemark(id)
        "post": "postBlogRemark",
    })),
    path("blog/<int:pk>/favorite/", BlogViewSet.as_view({
        "post": "favoriteBlog"  # favoriteBlog
    })),
]
