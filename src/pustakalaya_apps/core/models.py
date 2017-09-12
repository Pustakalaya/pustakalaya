from django.db import models
from django.utils.translation import ugettext as _
from .abstract_models import (
    AbstractTimeStampModel,
    AbstractBaseAuthor

)

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


class Publisher(AbstractTimeStampModel):
    publisher_name = models.CharField(
        _("Publisher name"),
        max_length=255
    )

    publisher_description = models.CharField(
        _("Publisher description"),
        max_length=255
    )

    class Meta:
        ordering = ("publisher_name",)

    def __str__(self):
        return self.publisher_name



class Keyword(AbstractTimeStampModel):
    keyword = models.CharField(
        max_length=255,
        verbose_name=_("Keyword")
    )

    keyword_description = models.TextField(
        verbose_name=_("Keyword description")
    )


class Biography(AbstractBaseAuthor):
    """Biography class to create an instace of document author, editor, illustrator,
    video director, video producer and audio recorder"""
    keywords = models.ManyToManyField(
         Keyword,
         verbose_name=_("Search Keywords")
     )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
