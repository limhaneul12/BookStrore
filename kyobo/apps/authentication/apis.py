from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from apps.store.apis import AuthorAbstractFilter

from .serializer import *
from .models import *
from .apis import *


class AdminAuthorOrgnaizationAPI(ListAPIView, AuthorAbstractFilter):
    queryset = PublisherAuthorOrganization.objects.all()
    serializer_class = PublisherOrganizationSerializer
    permission_classes = (IsAdminUser,)

