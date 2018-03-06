from django.contrib import admin
from .models import (
    Video,
    VideoSeries,
    VideoFileUpload,
    VideoLinkInfo
)


class VideoFileUploadAdmin(admin.TabularInline):
    model = VideoFileUpload
    extra = 1
    fields = ["upload"]


class AudioLinkInfoAdminInline(admin.StackedInline):
    model = VideoLinkInfo
    extra = 1


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = [
        AudioLinkInfoAdminInline,
        VideoFileUploadAdmin
    ]

    list_per_page = 10

    fields = (
        "title",
        "abstract",
        "collections",
        "education_levels",
        "languages",
        "place_of_publication",
        "publisher",
        "publication_year_on_text",
        "year_of_available_on_text",
        "video_running_time",
        "video_director",
        "video_producers",
        "video_certificate_license",
        "age",
        "video_genre",
        "keywords",
        "video_series",
        "volume",
        "edition",
        "published",
        "additional_note",
        "description",
        "license_type",
        "custom_license",
        "publication_year",
        "sponsors",
        "thumbnail"
    )


@admin.register(VideoSeries)
class VideoSeriesAdmin(admin.ModelAdmin):
    pass

