from django.db import models
from django.utils.translation import ugettext as _
from pustakalaya_apps.core.abstract_models import AbstractItem



class Audio(AbstractItem):
    """Audio class to store audio"""
    AUDIO_TYPE = (
        ('songs', _("Songs")),
        ('audio book', _("Audio Book"))
    )

    audio_type = models.CharField(
        choices=AUDIO_TYPE,
        max_length=12 #TODO replace dynamically.
    )


# Create your models here.
