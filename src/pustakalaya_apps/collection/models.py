from django.db import models
from django.utils.translation import ugettext as _
from pustakalaya_apps.core.abstract_models import AbstractTimeStampModel
from pustakalaya_apps.community.models import Community


class Collection(AbstractTimeStampModel):
    collection_name = models.CharField(
        _("Collection name"),
        max_length=255
    )

    collection_description = models.CharField(
        _("Collection description"),
        max_length=255
    )

    community = models.ForeignKey(
        Community,
        related_name="collections",
        on_delete=models.CASCADE,
        verbose_name=_("Community")
    )

    def __str__(self):
        return self.collection_name


