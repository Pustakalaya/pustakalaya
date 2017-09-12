#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractSeries,
    AbstractTimeStampModel

)

from pustakalaya_apps.core.models import (
    Category,
    Keyword,
    Biography,
)

class Video(AbstractItem):
    """Video item class"""

    video_category = models.ForeignKey(
        Category,
        verbose_name=_("Video Category")
    )

    video_director = models.ForeignKey(
        Biography,
        verbose_name=("Director"),
        related_name="directors"
    )

    video_producer = models.ManyToManyField(
        Biography,
        verbose_name=_("Producer"),
        related_name="producers"
    )


    video_series = models.ForeignKey(
        "VideoSeries",
        verbose_name=_("Video series"),
        on_delete=models.CASCADE
    )

    video_certificate_license = models.CharField(
        verbose_name=_("Certificate license name"),
        max_length=255
    )

    # TODO
    # cover_image = models.ImageField()




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