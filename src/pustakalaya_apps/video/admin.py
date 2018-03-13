from django.utils.html import format_html
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
    fields = ["file_name","upload"]


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

    search_fields = (
        'title',
    )

    list_display = ['title', 'preview_link']

    list_filter = ['title', 'published']

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
        "license",
        "custom_license",
        "sponsors",
        "thumbnail"
    )


    def preview_link(self, obj):
        return format_html("<a href='{url}'>Preview</a>", url=obj.get_absolute_url())


@admin.register(VideoSeries)
class VideoSeriesAdmin(admin.ModelAdmin):
    pass

