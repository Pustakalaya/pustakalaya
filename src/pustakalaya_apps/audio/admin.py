from django.utils.html import format_html
from django.contrib import admin
from .models import (
    AudioFileUpload,
    Audio,
    AudioGenre,
    AudioSeries,
    AudioLinkInfo,
    AudioType
)


class AudioFileUploadInline(admin.StackedInline):
    model = AudioFileUpload
    extra = 1
    fields = ["file_name","upload"]



class AudioLinkInfoAdminInline(admin.StackedInline):
    model = AudioLinkInfo
    extra = 1


@admin.register(Audio)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        AudioLinkInfoAdminInline,
        AudioFileUploadInline,
    ]

    list_filter = [ 'published']
    search_fields = (
        'title',
    )

    list_per_page = 10

    fields = (
        "title",
        "abstract",
        "collections",
        "education_levels",
        "languages",
        "place_of_publication",
        "publisher",
        "year_of_available_on_text",
        "publication_year_on_text",
        "audio_types",
        "audio_running_time",
        "audio_read_by",
        "published",
        "audio_genre",
        "keywords",
        "audio_series",
        "volume",
        "edition",
        "additional_note",
        "description",
        "license",
        "custom_license",
        "sponsors",
        "thumbnail"
    )

    list_display = ['title_link', 'published_',  'edit_link', 'updated_date_']

    def edit_link(self, obj):
        return format_html("<a href='{url}'>Edit</a>", url=obj.get_admin_url())

    def title_link(self,obj):
        return format_html('<a href="%s">%s</a>' %(obj.get_absolute_url(), obj.audio_title()))

    def published_(self,obj):
        return format_html('%s' % (obj.published_yes_no()))



    def updated_date_(self,obj):
        return format_html('%s' % (obj.updated_date_string()))


@admin.register(AudioGenre)
class AudioGenreAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


@admin.register(AudioSeries)
class AudioSeriesAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

@admin.register(AudioType)
class AudioTypeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
