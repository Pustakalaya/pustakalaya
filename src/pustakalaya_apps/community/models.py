from django.db import models
from django.utils.translation import ugettext as _
from pustakalaya_apps.core.abstract_models import AbstractTimeStampModel

class Community(AbstractTimeStampModel):
    community_name = models.CharField(
        _("Community name"),
        max_length=255
    )

    community_description = models.CharField(
        _("Community description"),
        max_length=255
    )

    def __str__(self):
        return self.community_name


