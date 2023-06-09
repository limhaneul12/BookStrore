from django.db import models
from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _

from apps.authentication.models import AuthorOrganizerInformation

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract: bool = True


class BooksAndPublicationYear(TimeStamp):
    author = models.ForeignKey(
        AuthorOrganizerInformation, verbose_name=_("author_id"), on_delete=models.CASCADE
    )
    book_name = models.CharField(
        max_length=40, verbose_name=_("book_name"), db_index=True
    )
    book_picture = models.ImageField(verbose_name=_("book_picture"))
    is_public = models.BooleanField(default=False, verbose_name=_("book_publishing"))
    publication_year = models.DateField()

    class Meta:
        db_table: str = "books_public_inform"

    def __str__(self) -> str:
        return f"[{self.book_name}]"


class BookContentDetailInform(TimeStamp):
    book_name = models.ForeignKey(
        BooksAndPublicationYear,
        verbose_name=_("book_name_id"),
        on_delete=models.CASCADE,
        db_index=True,
    )
    book_lang = models.CharField(max_length=15, verbose_name=_("book_lange"))
    content = models.CharField(
        max_length=40,
        verbose_name=_("book_content"),
        validators=[MaxLengthValidator(limit_value=40)],
    )

    class Meta:
        db_table: str = "content_detail_inform"

    def __str__(self) -> str:
        return f"[{self.book_name}]"
