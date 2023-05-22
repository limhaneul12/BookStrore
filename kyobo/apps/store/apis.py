from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializer import *


# Create your views here.
class AllBookInforViewset(ModelViewSet):
    queryset = AuthorInformation.objects.all()
    serializer_class = AuthorBookInformationSerializer
