from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from app01.activities.views import ActivityModelViewSet, ActivitySlideViewSet

router = DefaultRouter()
router.register('activity', ActivityModelViewSet)
router.register('slider', ActivitySlideViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('activity/<int:pk>/join/',)
]
