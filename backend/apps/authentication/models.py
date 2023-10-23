from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


# Create your models here.


class AuthorInformation(models.Model):
    author = models.CharField(max_length=15, null=False, verbose_name=_("author"))
    nationality = CountryField()

    publisher = models.ForeignKey(to="publisher", null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table: str = "author_organizer"
        db_table_comment: str = "저자 테이블"

        indexes: list[models.Index] = [
            models.Index(fields=["author"], name="author_index")
        ]

    def __str__(self) -> str:
        return f"[{self.author}]"


class Publisher(models.Model):
    publisher = models.CharField(max_length=40, verbose_name=_("publisher"))
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table: str = "author_publisher"
        db_table_comment: str = "출판사 테이블"

        indexes: list[models.Index] = [
            models.Index(fields=["publisher"], name="publisher_index")
        ]

    def __str__(self) -> str:
        return f"[{self.publisher}]"
