from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


# Create your models here.
class PublisherAuthorOrganization(models.Model):
    publisher = models.CharField(
        max_length=40, verbose_name=_("publisher"), db_index=True
    )
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table: str = "author_publisher"

    def __str__(self) -> str:
        return f"[{self.publisher}]"


class AuthorOrganizerInformation(models.Model):
    author = models.CharField(
        max_length=15, null=False, verbose_name=_("author"), db_index=True
    )
    publisher = models.ForeignKey(
        PublisherAuthorOrganization,
        verbose_name=_("publisher_id"),
        on_delete=models.CASCADE,
    )
    nationality = CountryField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table: str = "author_organizer"
    def __str__(self) -> str:
        return f"[{self.author}]"
