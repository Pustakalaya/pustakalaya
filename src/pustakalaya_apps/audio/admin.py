from django.contrib import admin
from .models import (
    AudioFileUpload,
    Audio,
    AudioGenre,
    AudioSeries
)


class AudioFileUploadInline(admin.StackedInline):
    model = AudioFileUpload


@admin.register(Audio)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        AudioFileUploadInline,
    ]



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
