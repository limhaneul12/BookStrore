from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PublisherAuthorOrganization)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ["publisher"]


@admin.register(AuthorOrganizerInformation)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["author", "publisher_id"]
