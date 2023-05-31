from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("tasks", views.TaskViewSet)
urlpatterns = [
    path("", views.index),
    path("about-us", views.about),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
