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


admin.site.register(AudioGenre)
admin.site.register(AudioSeries)
