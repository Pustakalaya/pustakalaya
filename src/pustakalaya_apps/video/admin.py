from django.contrib import admin
from .models import (
    Video,
    VideoSeries
)

# Register your models here.
admin.site.register(Video)
admin.site.register(VideoSeries)

