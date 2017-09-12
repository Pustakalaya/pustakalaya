from django.contrib import admin
from .models import (
    AudioFileUpload,
    Audio
)


class AudioFileUploadInline(admin.StackedInline):
    model = AudioFileUpload


@admin.register(Audio)
class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        AudioFileUploadInline,
    ]
