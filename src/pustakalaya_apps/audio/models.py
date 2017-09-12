from django.db import models
from django.utils.translation import ugettext as _
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractBaseAuthor,
    AbstractTimeStampModel,
    AbstractSeries
)
from pustakalaya_apps.core.models import (
    Category,
    Keyword,
    Publisher,
    Biography
)
from pustakalaya_apps.collection.models import Collection


class Audio(AbstractItem):
    """Audio class to store audio"""
    AUDIO_TYPE = (
        ('audio book', _("Audio Book")),
    )

    audio_type = models.CharField(
        verbose_name=_("Audio type"),
        choices=AUDIO_TYPE,
        max_length=12  # TODO replace dynamically.
    )

    collection = models.ManyToManyField(
        Collection,
        verbose_name=_("Add this audio to these collection")
    )

    type = models.CharField(
        default="audio",
        max_length=255,
        editable=False
    )
    audio_running_time = models.TimeField(
        _("Running time")
    )

    # TODO file size
    # Like that format the given no in MB, KB, GB for entered MB size

    audio_read_by = models.ForeignKey(
        Biography,
        verbose_name=_("Read / Voice by"),

    )

    publisher = models.ForeignKey(
        Publisher,
        verbose_name=_("Audio publisher")
    )

    audio_category = models.ForeignKey(
        Category,
        verbose_name=_("Audio Category")
    )

    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Select list of keywords")
    )

    audio_genre = models.ForeignKey(
        "AudioGenre",
        verbose_name=_("Audio Genre")
    )

    audio_series = models.ForeignKey(
        'AudioSeries',
        verbose_name=_("Audio Series / Volume")
    )

    def __str__(self):
        return self.title


class AudioGenre(AbstractTimeStampModel):
    genre = models.CharField(
        _("Genre name"),
        max_length=255
    )

    genre_description = models.TextField(
        verbose_name=_("Genre description")
    )

class AudioSeries(AbstractSeries):
    def __str__(self):
        return "{}".format(self.series_name)



class AudioFileUpload(AbstractTimeStampModel):
    """Class to upload the multiple document objects"""

    file_name = models.CharField(
        _("File name"),
        max_length=255,
    )

    audio = models.ForeignKey(
        Audio,
        on_delete=models.CASCADE
    )

    upload = models.FileField(
        upload_to="uploads/audio/%Y/%m/",
        max_length=255
    )

    def __str__(self):
        return self.file_name
