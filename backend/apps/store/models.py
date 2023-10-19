from django.db import models
from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract: bool = True


class BooksAndPublicationYear(TimeStamp):
    author = models.ForeignKey(
        to="authentication.AuthorInformation", 
        verbose_name=_("author_id"), 
        on_delete=models.CASCADE
    )
    book_name = models.CharField(
        max_length=40, 
        verbose_name=_("book_name"),
        unique=True,
    )
    book_picture = models.ImageField(verbose_name=_("book_picture"))
    is_public = models.BooleanField(default=False, verbose_name=_("book_publishing"))
    publication_year = models.DateField()

    class Meta:
        db_table: str = "books_public_inform"
        db_table_comment: str = "책 정보 테이블"
        indexes: list[models.Index] = [
            models.Index(fields=["book_name"], name="book_name_index")
        ]

    def __str__(self) -> str:
        return f"[{self.book_name}]"


class BookContentDetailInform(TimeStamp):
    book_name = models.OneToOneField(
        to="BooksAndPublicationYear",
        verbose_name=_("book_name_id"),
        on_delete=models.CASCADE,
    )
    nationality = CountryField(null=False)
    content = models.CharField(
        max_length=40,
        verbose_name=_("book_content"),
        validators=[MaxLengthValidator(limit_value=40)],
    )

    class Meta:
        db_table: str = "content_detail_inform"
        db_table_comment: str = "책언어 테이블"
        indexes: list[models.Index] = [
            models.Index(fields=["book_name"], name="bookname_fore_index"),
            models.Index(fields=["nationality"], name="nationlity_index")
        ]

    def __str__(self) -> str:
        return f"[{self.book_name}]"
