from rest_framework import serializers
from .models import *


class AuthorBookInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorOrganizerInformation
        fields = [
            "author",
            "nationality",
        ]
        

class PublisherOrganizationSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    class Meta:
        model = PublisherAuthorOrganization
        fields = [
            "id",
            "publisher", 
            "author"
        ]
    
    def get_author(self, obj):
        author = AuthorOrganizerInformation.objects.filter(publisher=obj)
        return AuthorBookInformationSerializer(author, many=True).data
