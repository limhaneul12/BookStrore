from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import apis
from .serializer import *


router = DefaultRouter()
router.register("", apis.AllBookInforViewset)

urlpatterns = [
    path("", include(router.urls))
]
