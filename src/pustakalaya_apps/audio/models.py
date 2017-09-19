from django.db import models
from django.utils.translation import ugettext as _

from pustakalaya_apps.collection.models import Collection
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractTimeStampModel,
    AbstractSeries
)
from pustakalaya_apps.core.models import (
    Category,
    Keyword,
    Publisher,
    Biography,
    Sponsor
)
from .search import AudioDoc


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
        verbose_name=_("Add this audio to these collection"),
    )

    type = models.CharField(
        default="audio",
        max_length=5,
        editable=False
    )
    audio_running_time = models.CharField(
        verbose_name=_("Running time in minutes"),
        max_length=3
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

    sponsors = models.ManyToManyField(
        Sponsor,
        verbose_name=_("Sponsor")
    )

    audio_thumbnail = models.ImageField(
        upload_to="uploads/thumbnails/audio/%Y/%m/%d",
        max_length=255
    )



    def doc(self):
        obj = AudioDoc(
            meta={'id': self.id},
            id=self.id,
            title=self.title,
            abstract=self.abstract,
            type=self.type,
            education_level=self.education_level,
            category=self.category,
            language=self.language,
            additional_note=self.additional_note,
            description=self.description,
            license_type=self.license_type,
            year_of_available=self.year_of_available,
            date_of_issue=self.date_of_issue,
            place_of_publication=self.place_of_publication,
            created_date=self.created_date,
            updated_date=self.updated_date,
            # Common fields in document, audio and video library
            publisher=self.publisher.publisher_name,
            sponsors=[sponsor.name for sponsor in self.sponsors.all()],  # Multi value # TODO some generators
            collections=[c.collection_name for c in self.collection.all()],  # ToDO generator
            keywords=[keyword.keyword for keyword in self.keywords.all()],

            # Audio type specific
            audio_category=self.audio_category.category_name,
            audio_running_time=self.audio_running_time,
            audio_thumbnail=self.audio_thumbnail.name,
            audio_read_by = self.audio_read_by.getname,
            audio_series=self.audio_series.series_name,
        )

        return obj

    def index(self):
        """index all the document to elastic search index server"""
        self.doc().save()
        return self.doc().to_dict(include_meta=True)

    def delete_index(self):
        try:
            self.doc().delete()
        except Exception as e:
            print(e)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "audio"


class AudioGenre(AbstractTimeStampModel):
    genre = models.CharField(
        _("Genre name"),
        max_length=255
    )

    genre_description = models.TextField(
        verbose_name=_("Genre description")
    )

    class Meta:
        db_table = "audio_genre"

    def __str__(self):
        return self.genre

class AudioSeries(AbstractSeries):
    def __str__(self):
        return "{}".format(self.series_name)

    class Meta:
        db_table = "audio_series"


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


    class Meta:
        db_table = "audio_file"
