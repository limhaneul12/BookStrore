from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .serializer import *
from .models import *
from .apis import *


class AuthorAbstractFilter:
    """
    filter abstract
    추상화 작성 pagenation 추가 고민
    """

    filters_backends = [DjangoFilterBackend]
    filters_fields = ["author"]


class AdminAuthorOrgnaizationAPI(ListAPIView, AuthorAbstractFilter):
    queryset = PublisherAuthorOrganization.objects.all()
    serializer_class = PublisherOrganizationSerializer
    permission_classes = (IsAdminUser,)

