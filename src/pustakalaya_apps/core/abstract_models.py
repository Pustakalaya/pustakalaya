# Modules that host all abstract class.

from django.db import models
from django.utils.translation import ugettext as _
# from pustakalaya_apps.collection.models import Collection


# from .models import ItemCategory


class AbstractTimeStampModel(models.Model):
    """TimeStampModel that holds created_date and updated_date field"""

    created_date = models.DateTimeField(_("Created date"), auto_now_add=True)
    updated_date = models.DateTimeField(_("Updated date"), auto_now=True)

    def __str__(self):
        return self.created_date

    class Meta:
        abstract = True


class AbstractBaseAuthor(AbstractTimeStampModel):
    """Base author class that holds the common attributes for other author class."""

    first_name = models.CharField(_("First name"), max_length=255)
    last_name = models.CharField(_("Last name"), max_length=255)

    def __str__(self):
        return self.first_name

    class Meta:
        abstract = True


class AbstractSeries(AbstractTimeStampModel):
    """Abstract Series models for data item"""
    series_name = models.CharField(
        _("Series name"),
        max_length=255
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

    ITEM_INTERACTIVE_TYPE = (
        ("interactive", _("Interactive")),
        ("noninteractive", _("Non interactive")),
    )



    item_title = models.CharField(
        _("Title"),
        max_length=255,
        unique=True
    )

    item_abstract = models.TextField(
        _("Item abstract")
    )



    item_label = models.CharField(
        _("Education Level"),
        max_length=255,
        choices=ITEM_LABEL

    )

    item_interactivity = models.CharField(
        _("Item Interactive"),
        max_length=15,
        choices=ITEM_INTERACTIVE_TYPE
    )

    #
    # item_category = models.ManyToManyField(
    #     ItemCategory,
    #     verbose_name=_("Item category")
    # )

    item_language = models.CharField(
        _("Item Language"),
        choices=(
            ("nepali", _("Nepali")),
            ("english", _("English")),
        ),
        max_length=255  # TODO
    )

    item_citation = models.CharField(
        _("Citation"),
        max_length=255,
        blank=True
    )

    item_reference_link = models.URLField(
        _('Item reference link'),
        blank=True
    )

    item_additional_node = models.TextField(
        _("Additional Note"),
        blank=True
    )

    item_sponsors = models.CharField(
        _("Sponsors"),
        max_length=255,
        blank=True,
    )

    item_description = models.TextField(
        _("Item description"),
    )

    item_license_type = models.CharField(
        _("Item license type"),
        choices=ITEM_LICENSE_TYPE,
        max_length=255,
    )

    item_custom_license = models.TextField(
        _("Item custom license"),
        blank=True
    )

    item_years_of_available = models.DateField(
        _("Years of available"),
        blank=True
    )

    item_date_of_issue = models.DateField(
        _("Item date of issue"),
        blank=True
    )

    item_identifier_type = models.CharField(
        _("Item identifier type"),
        choices=(
            ("issn", _("ISSN")),
            ("ismn", _("ISMN")),
            ("govt doc", _("Gov't Doc")),
            ("uri", _("URI")),
            ("isbn", _("ISBN"))
        ),
        max_length=255  # TODO
    )

    item_place_of_publication = models.CharField(
        _("Place of publication"),
        max_length=255,
        blank=True
    )

    # Rating TODO

    # Comment TODO


    # Keyword TODO: ManyToManyField

    # FileUpload ForeignKey.

    class Meta:
        abstract = True
