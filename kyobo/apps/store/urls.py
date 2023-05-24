from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import apis
from .serializer import *


router = DefaultRouter()
router.register(
    "private", apis.AllAuthorTotalInformationViewset, basename="private-book"
)


urlpatterns = [
    path("author/", include(router.urls)),
    path("public-book", apis.PublicBookReslses.as_view(), name="public_book"),
]
