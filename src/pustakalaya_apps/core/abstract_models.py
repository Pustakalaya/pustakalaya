# Modules that host all abstract class.

import uuid

from django.db import models
from django.utils.translation import ugettext as _


# from pustakalaya_apps.collection.models import Collection


# from .models import ItemCategory


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

    first_name = models.CharField(_("First name"), max_length=255)
    middle_name = models.CharField(_("Middle name"), max_length=255, blank=True)
    last_name = models.CharField(_("Last name"), max_length=255)
    description = models.TextField(
        _("Description")
    )
    dob = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True
    )
    pen_name = models.CharField(
        verbose_name=_("Pen name"),
        max_length=255
    )
    address = models.TextField(
        verbose_name=_("Address")
    )

    genre = models.TextField(
        verbose_name=_("Genre"),
        max_length=100
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
    ITEM_LABEL = (
        ("early primary level", _("Early primary level")),
        ("primary level", _("Primary level")),
        ("Middle school level", _("Middle school level")),
        ("highschool level", _("Highschool level")),
        ("intermediate level", _("Intermediate level")),
    )

    ITEM_LICENSE_TYPE = (
        ("creative commons", _("Creative Commons")),
        ("copyright retained", _("Copyright retained")),
        ("apache License 2.0", _("Apache License 2.0")),
        ("creative commons", _("Creative Commons")),
        ("mit license", _("MIT License")),
    )

    TYPE = (
        ("document", _("Document")),
        ("audio", _("Audio")),
        ("video", _("Video")),
        ("image", _("Image")),
        ("wikipedia", _("Wikipedia")),
        ("map", _("Map")),
    )

    CATEGORY = (
        ("literatures and arts", _("Literature and arts")),
        ("course materials", _("Course materials")),
        ("teaching materials", _("Teaching materials")),
        ("reference materials", _("Reference materials")),
    )

    title = models.CharField(
        _("Title"),
        max_length=255,
        unique=True
    )

    abstract = models.TextField(
        _("Abstract")
    )

    education_level = models.CharField(
        _("Education Level"),
        max_length=255,
        choices=ITEM_LABEL

    )

    category = models.CharField(
        choices=CATEGORY,
        max_length=255
    )

    language = models.CharField(
        _("Language"),
        choices=(
            ("nepali", _("Nepali")),
            ("english", _("English")),
        ),
        max_length=255  # TODO
    )

    citation = models.CharField(
        _("Citation"),
        max_length=255,
        blank=True
    )

    reference_link = models.URLField(
        _('Reference link'),
        blank=True
    )

    additional_note = models.TextField(
        _("Additional Note"),
        blank=True
    )

    # TODO: sponsors should be listed in every model.

    description = models.TextField(
        _("Description"),
    )

    license_type = models.CharField(
        _("License type"),
        choices=ITEM_LICENSE_TYPE,
        max_length=255,
    )

    custom_license = models.TextField(
        _("Custom license"),
        blank=True
    )

    year_of_available = models.DateField(
        _("Year of available"),
        blank=True,
        null=True
    )

    date_of_issue = models.DateField(
        _("Date of issue"),
        blank=True,
        null=True
    )

    place_of_publication = models.CharField(
        _("Place of publication"),
        max_length=255,
        blank=True
    )

    # Rating TODO

    # Comment TODO

    # Grade TODO

    # Keyword TODO: ManyToManyField

    # FileUpload ForeignKey.

    class Meta:
        abstract = True
