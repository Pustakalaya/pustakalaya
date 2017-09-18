from django.apps import AppConfig


class VideoConfig(AppConfig):
    name = 'pustakalaya_apps.video'

    def ready(self):
        from . import signals