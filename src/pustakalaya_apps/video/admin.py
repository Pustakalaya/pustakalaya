from django.contrib import admin
from .models import (
    Video,
    VideoSeries,
    VideoFileUpload
)


class VideoFileUploadAdmin(admin.TabularInline):
    model = VideoFileUpload
    extra = 1


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = [
        VideoFileUploadAdmin
    ]


@admin.register(VideoSeries)
class VideoSeriesAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
