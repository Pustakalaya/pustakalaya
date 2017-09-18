from django.apps import AppConfig


class AudioConfig(AppConfig):
    name = 'pustakalaya_apps.audio'

    def ready(self):
        from . import signals
