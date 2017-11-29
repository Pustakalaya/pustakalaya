# Modules that host all abstract class.

import uuid
import abc

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .constants import LANGUAGES


class AbstractTimeStampModel(models.Model):
    """TimeStampModel that holds created_date and updated_date field"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("Updated date"), auto_now=True)

    def __str__(self):
        return self.created_date

    class Meta:
        abstract = True


class AbstractBaseAuthor(AbstractTimeStampModel):
    """Base author class that holds the common attributes for other author class."""

    first_name = models.CharField(
        _("First name"),
        max_length=255,
    )
    middle_name = models.CharField(_("Middle name"), max_length=255, blank=True)
    last_name = models.CharField(_("Last name"), max_length=255)
    description = models.TextField(
        _("Description"),
        blank=True,
    )
    dob = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True,
        null=True
    )
    pen_name = models.CharField(
        verbose_name=_("Pen name"),
        max_length=255,
        blank=True
    )
    address = models.TextField(
        verbose_name=_("Address"),
        blank=True
    )

    genre = models.CharField(
        verbose_name=_("Genre"),
        max_length=100,
        blank = True
    )

    thumbnail = models.ImageField(
        verbose_name=_("Creator image"),
        blank=True,
        null=True,
        upload_to="uploads/creator"
    )

    @property
    def getname(self):
        return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)

    def __str__(self):
        return self.first_name

    class Meta:
        abstract = True


class AbstractSeries(AbstractTimeStampModel):
    """Abstract Series models for data item"""

    class Meta:
        abstract = True

    series_name = models.CharField(
        _("Series name"),
        max_length=255
    )

    description = models.TextField(
        verbose_name=_("Description")
    )

    class Meta:
        abstract = True


class AbstractItem(AbstractTimeStampModel):
    """Item base class that share common attributes for digital item"""

    ITEM_LICENSE_TYPE = (
        ("creative commons", _("Creative commons")),
        ("copyright retained", _("Copyright retained")),
        ("apache License 2.0", _("Apache license 2.0")),
        ("creative commons", _("Creative commons")),
        ("mit license", _("MIT License")),
        ("custom license", _("Custom License")),
        ("na", _("Not available")),
    )

    TYPE = (
        ("document", _("Document")),
        ("audio", _("Audio")),
        ("video", _("Video")),
        ("image", _("Image")),
        ("wikipedia", _("Wikipedia")),
        ("map", _("Map")),
    )

    title = models.CharField(
        _("Title"),
        max_length=255,
    )

    abstract = models.TextField(
        _("Abstract/Summary"),
        blank=True
    )

    # TODO: Implemenet in second phase with Marc21 format.
    # citation = models.CharField(
    #     _("Citation"),
    #     max_length=255,
    #     blank=True
    # )

    additional_note = models.TextField(
        _("Additional Note"),
        blank=True
    )

    # TODO: sponsors should be listed in every model.

    description = models.TextField(
        _("Description"),
        blank=True
    )

    license_type = models.CharField(
        _("License type"),
        choices=ITEM_LICENSE_TYPE,
        max_length=255,
    )

    custom_license = models.TextField(
        _("Rights"),
        blank=True
    )

    year_of_available = models.DateField(
        _("Year of available"),
        blank=True,
        null=True
    )

    publication_year = models.DateField(
        _("Publication year"),
        blank=True,
        null=True
    )

    place_of_publication = models.CharField(
        _("Place of publication"),
        max_length=255,
        blank=True
    )

    volume = models.CharField(
        max_length=254,
        default="",
        blank=True
    )

    edition = models.CharField(
        max_length=254,
        default="",
        blank=True
    )

    featured = models.CharField(
        verbose_name=_("Featured"),
        max_length=3,
        default="no",
        choices=(
            ("yes", _("Yes")),
            ("no", _("No"))
        )
    )


    class Meta:
        abstract = True

    def doc(self):
        return dict(
            meta={'id': self.id},
            id=self.id,

            title = self.title,
            title_suggest={"input": [self.title]},
            abstract=self.abstract,
            license_type=self.license_type,
            description=self.description,
            year_of_available=self.year_of_available,
            publication_year=self.publication_year,
            created_date=self.created_date,
            updated_date=self.updated_date,
            view_count = self.get_view_count
        )

    @abc.abstractmethod
    def bulk_index(self):
        """
        Call this method to index an instance to index server.
        """
        pass

    @property
    def get_view_count(self):
        return 0


class LinkInfo(AbstractTimeStampModel):
    link_name = models.URLField(
        verbose_name=_("Link URL")
    )

    link_description = models.CharField(
        max_length=500,
        verbose_name=_("Link Description")
    )

    class Meta:
        abstract = True
