# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _
from pustakalaya_apps.collection.models import Collection
from elasticsearch.exceptions import NotFoundError
from .search import VideoDoc
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractSeries,
    AbstractTimeStampModel,
    LinkInfo

)

from pustakalaya_apps.core.models import (
    Keyword,
    Biography,
    Sponsor,
    Publisher,
    Language,
    EducationLevel,
)


class Video(AbstractItem):
    """
    Video item class
    """

    collections = models.ManyToManyField(
        Collection,
        verbose_name=_("Add this video to these collection"),
    )

    video_director = models.ForeignKey(
        Biography,
        verbose_name=("Director"),
        related_name="directors",
        blank=True,
        null=True
    )

    video_producers = models.ManyToManyField(
        Biography,
        verbose_name=_("Producer"),
        related_name="producers",
        blank=True,
        null=True
    )

    education_levels = models.ManyToManyField(
        EducationLevel,
        verbose_name=_("Education Level")
    )
    languages = models.ManyToManyField(
        Language,
        verbose_name=_("Languages")
    )

    video_series = models.ForeignKey(
        "VideoSeries",
        verbose_name=_("Video series"),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    type = models.CharField(
        editable=False,
        default="video",
        max_length=4
    )
    video_certificate_license = models.CharField(
        verbose_name=_("Certification"),
        max_length=255,
        blank=True
    )
    age = models.CharField(
        verbose_name=_("Age group"),
        max_length=255,
        blank=True,
    )

    sponsors = models.ManyToManyField(
        Sponsor,
        verbose_name=_("Sponsor"),
        blank=True,
        null=True
    )

    video_genre = models.ForeignKey(
        "VideoGenre",
        verbose_name=_("Video Genre"),
        blank=True,
        null=True
    )

    publisher = models.ForeignKey(
        Publisher,
        verbose_name=_("Publisher"),
    )

    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Keywords"),
        blank=True
    )

    thumbnail = models.ImageField(
        upload_to="uploads/thumbnails/video/%Y/%m/%d",
        max_length=255,
        blank=True
    )

    video_running_time = models.CharField(
        verbose_name=_("Running time in minutes"),
        max_length=3,
        blank=True,
        default="0"
    )

    @property
    def getauthors(self):
        author_list = [(author.getname, author.pk) for author in [self.video_director]]
        return author_list or [None]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("video:detail", kwargs={"title": slugify(self.title), "pk": self.pk})

    def doc(self):
        # Parent attr
        item_attr = super(Video, self).doc()
        # Combine item attr and video attr to index in search server
        videoattr = dict(
            **item_attr,
            publisher=self.publisher.publisher_name,
            sponsors=[sponsor.name for sponsor in self.sponsors.all()],  # Multi value # TODO some generators
            keywords=[keyword.keyword for keyword in self.keywords.all()],
            type=self.type,
            education_levels=[education_level.level for education_level in self.education_levels.all()],
            communities=[collection.community_name for collection in self.collections.all()],
            collections=[collection.collection_name for collection in self.collections.all()],
            languages=[language.language.lower() for language in self.languages.all()],
            video_running_time=self.video_running_time,
            thumbnail=self.thumbnail.name,
            video_director=getattr(self.video_director, "getname", ""),
            video_series=getattr(self.video_series, "series_name", ""),
            video_certificate_license=self.video_certificate_license,
            video_genre=getattr(self.video_genre, "genre", ""),
            author_list=self.getauthors,
            url = self.get_absolute_url()

        )
        # Create a video  instance
        obj = VideoDoc(**videoattr)
        return obj

    def index(self):
        """
        Call this method to index an instance to search server
        """
        # Save video instance
        self.doc().save()

    def bulk_index(self):
        """
        call this method to during bulk indexing an instance to search server.
        method used by `search.py module`
        """
        return self.doc().to_dict(include_meta=True)

    def delete_index(self):
        """method to delete a video instance from search server
        This method is called by `signals.py` module
        """
        try:
            self.doc().delete()
        except NotFoundError:
            pass

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


class VideoLinkInfo(LinkInfo):
    video = models.ForeignKey(
        Video,
        verbose_name=_("Link"),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.video.title


class VideoGenre(AbstractTimeStampModel):
    genre = models.CharField(
        _("Genre name"),
        max_length=255
    )

    genre_description = models.TextField(
        verbose_name=_("Genre description")
    )

    class Meta:
        db_table = "video_genre"

    def __str__(self):
        return self.genre
