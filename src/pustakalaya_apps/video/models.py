# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from pustakalaya_apps.collection.models import Collection
from .search import VideoDoc
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractSeries,
    AbstractTimeStampModel

)

from pustakalaya_apps.core.models import (
    Category,
    Keyword,
    Biography,
    Sponsor,
    Publisher
)


class Video(AbstractItem):
    """
    Video item class
    """

    video_category = models.ForeignKey(
        Category,
        verbose_name=_("Video Category")
    )

    collection = models.ManyToManyField(
        Collection,
        verbose_name=_("Add this audio to these collection"),
    )

    video_director = models.ForeignKey(
        Biography,
        verbose_name=("Director"),
        related_name="directors"
    )

    video_producers = models.ManyToManyField(
        Biography,
        verbose_name=_("Producer"),
        related_name="producers"
    )

    video_series = models.ForeignKey(
        "VideoSeries",
        verbose_name=_("Video series"),
        on_delete=models.CASCADE
    )

    type = models.CharField(
        editable=False,
        default="video",
        max_length=4
    )
    video_certificate_license = models.CharField(
        verbose_name=_("Certificate license name"),
        max_length=255
    )

    sponsors = models.ManyToManyField(
        Sponsor,
        verbose_name=_("Sponsor")
    )

    publisher = models.ForeignKey(
        Publisher,
        verbose_name=_("Publisher"),
    )

    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Keywords")
    )

    video_thumbnail = models.ImageField(
        upload_to="uploads/thumbnails/video/%Y/%m/%d",
        max_length=255
    )

    video_running_time = models.CharField(
        verbose_name=_("Running time in minutes"),
        max_length=3
    )

    def doc(self):
        obj = VideoDoc(
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

            # Document type specific
            video_category=self.video_category.category_name,
            video_running_time=self.video_running_time,
            video_thumbnail=self.video_thumbnail.name,
            video_director=self.video_director.getname,
            video_series=self.video_series.series_name,
            video_certificate_license=self.video_certificate_license
        )
        return obj

    def index(self):
        """index all the document to elastic search index server"""

        self.doc().save()
        return self.doc().to_dict(include_meta=True)

    def delete_index(self):

        self.doc().delete()

    def __str__(self):
        return self.title


class VideoSeries(AbstractSeries):
    def __str__(self):
        return "{}".format(self.series_name)


class VideoFileUpload(AbstractTimeStampModel):
    """Class to upload the multiple document objects"""

    file_name = models.CharField(
        _("File name"),
        max_length=255,
    )

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE
    )

    upload = models.FileField(
        upload_to="uploads/videos/%Y/%m/",
        max_length=255
    )

    def __str__(self):
        return self.file_name
