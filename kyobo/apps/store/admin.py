from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(BooksAndPublicationYear)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["is_public", "book_name", "author", "created_at"]
    list_display_links = ["book_name"]
    search_fields = ["book_name"]

    list_filter = ["is_public"]


@admin.register(BookContentDetailInform)
class BookContenPublicationAdmin(admin.ModelAdmin):
    list_display = ["book_name", "book_lang"]
    list_display_links = ["book_name"]
    search_fields = ["book_name"]

    list_filter = ["book_lang"]
