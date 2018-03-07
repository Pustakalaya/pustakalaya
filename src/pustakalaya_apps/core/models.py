from django.db import models
from django.utils.translation import ugettext as _
from .abstract_models import (
    AbstractTimeStampModel,
    AbstractBaseAuthor

)
from .constants import LANGUAGES


class Category(AbstractTimeStampModel):
    category_name = models.CharField(
        _("Category name"),
        max_length=255,
    )

    category_description = models.TextField(
        verbose_name=_("Category description")
    )

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "category"


class Publisher(AbstractTimeStampModel):
    publisher_name = models.CharField(
        _("Publisher name"),
        max_length=255,
        unique=True,
    )

    publisher_description = models.CharField(
        _("Publisher description"),
        max_length=255
    )

    class Meta:
        ordering = ("publisher_name",)
        db_table = "publisher"

    def __str__(self):
        return self.publisher_name


class Keyword(AbstractTimeStampModel):
    keyword = models.CharField(
        max_length=255,
        verbose_name=_("Keyword"),
        unique=True
    )

    keyword_description = models.TextField(
        verbose_name=_("Keyword description"),
        blank=True,
        default=""
    )

    def __str__(self):
        return self.keyword

    class Meta:
        db_table = "keyword"


class Biography(AbstractBaseAuthor):
    """Biography class to create an instance of document author, editor, illustrator,
    video director, video producer and audio recorder"""
    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Search Keywords"),
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "biography"
        verbose_name = _("Author")
        ordering = ['first_name']


class Sponsor(AbstractTimeStampModel):
    name = models.CharField(
        max_length=200,
        verbose_name=_("Sponsor Name"),
        unique=True
    )

    description = models.TextField(
        verbose_name=_("Description")
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sponsor"


class EducationLevel(models.Model):
    """Education level"""

    EDUCATION_LEVEL = (
        ("early primary level", _("Early primary level")),
        ("primary level", _("Primary level")),
        ("Middle school level", _("Middle school level")),
        ("highschool level", _("Highschool level")),
        ("intermediate level", _("Intermediate level")),
    )

    level = models.CharField(
        _("Education Level"),
        max_length=255,
        choices=EDUCATION_LEVEL,
        unique=True

    )

    description = models.CharField(
        max_length=500,
        blank=True
    )

    def __str__(self):
        return self.level

    class Meta:
        db_table = "education_level"


class Language(models.Model):
    language = models.CharField(
        choices=LANGUAGES,
        max_length=7,
        verbose_name=_("Language"),
        unique=True

    )

    class Meta:
        db_table = "language"

    def __str__(self):
        return u"%s" % (self.get_language_display())
