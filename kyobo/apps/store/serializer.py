from rest_framework import serializers
from apps.authentication.models import AuthorOrganizerInformation
from typing import *
from .models import *


class ContentBookInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookContentDetailInform
        fields = [
            "book_lang",
            "content",
        ]


class BookInformationSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = BooksAndPublicationYear
        fields = [
            "book_name",
            "publication_year",
            "is_public",
            "content",
        ]

    def get_content(self, obj):
        content = BookContentDetailInform.objects.filter(book_name=obj)
        return ContentBookInformationSerializer(content, many=True).data


class AuthorBookInformationSerializer(serializers.ModelSerializer):
    book_info = serializers.SerializerMethodField()

    class Meta:
        model = AuthorOrganizerInformation
        fields = [
            "id",
            "author",
            "nationality",
            "book_info",
            "created_at",
            "updated_at",
        ]

    def get_book_info(self, obj):
        book_info = BooksAndPublicationYear.objects.filter(author_id=obj)
        return BookInformationSerializer(book_info, many=True).data
