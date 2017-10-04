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


class AudioLinkInfoAdminInline(admin.StackedInline):
    model = VideoLinkInfo
    extra = 1


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = [
        AudioLinkInfoAdminInline,
        VideoFileUploadAdmin
    ]

    fields = (
        "title",
        "abstract",
        "collection",
        "education_levels",
        "language",
        "place_of_publication",
        "publisher",
        "year_of_available",
        "keywords",
        "volume",
        "edition",
        "additional_note",
        "description",
        "license_type",
        "custom_license",
        "date_of_issue",
        "sponsors",
    )


@admin.register(VideoSeries)
class VideoSeriesAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
