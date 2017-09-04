from django.db import models
from django.utils.translation import ugettext as _
from pustakalaya_apps.core.abstract_models import AbstractTimeStampModel

class Community(AbstractTimeStampModel):
    collection_name = models.CharField(
        _("Collection name"),
        max_length=255
    )

    collection_description = models.CharField(
        _("Collection description"),
        max_length=255
    )

    def __str__(self):
        return self.collection_name


