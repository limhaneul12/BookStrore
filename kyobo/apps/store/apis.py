from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import *
from .serializer import *


# Create your views here.
class AuthorAbstractFilter:
    """
    filter abstract
    추상화 작성 pagenation 추가 고민
    """

    filters_backends = [DjangoFilterBackend]
    filters_fields = ["author"]


class AllAuthorTotalInformationViewset(ModelViewSet, AuthorAbstractFilter):
    """
    Args:
        ModelViewSet (_type_): CRUD
        AuthorAbstractFilter (_type_): 필터 추상화
    """

    queryset = AuthorInformation.objects.all()
    serializer_class = AuthorBookInformationSerializer
    permission_classes = (IsAdminUser,)


class PublicBookReslses(ListAPIView, AuthorAbstractFilter):
    """
    Args:
        ListAPIView (_type_): 출시 완료된 도서만
        AuthorAbstractFilter (_type_): 필터 추상화
    """

    queryset = BooksAndPublicationYear.objects.filter(is_public=True)
    serializer_class = BookInformationSerializer
    permission_classes = (AllowAny,)
