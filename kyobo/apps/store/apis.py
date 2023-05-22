from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import *
from .serializer import *


# Create your views here.
class AuthorAbstractFilter:
    filters_backends = [DjangoFilterBackend]
    filters_fields = ["author"]


class AllAuthorTotalInformationViewset(ModelViewSet, AuthorAbstractFilter):
    queryset = AuthorInformation.objects.all()
    serializer_class = AuthorBookInformationSerializer
    permission_classes = (IsAdminUser, )


class PublicBookReslses(ListAPIView, AuthorAbstractFilter):
    queryset = BooksAndPublicationYear.objects.filter(is_public=True) 
    serializer_class = BookInformationSerializer
    permission_classes = (AllowAny, )
