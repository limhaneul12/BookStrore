from django.urls import path 
from . import apis

urlpatterns = [
    path(
        "private-author",
        apis.AdminAuthorOrgnaizationAPI.as_view(),
        name="private_author",
    ),
]
