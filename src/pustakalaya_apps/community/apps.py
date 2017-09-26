from django.apps import AppConfig


class CommunityConfig(AppConfig):
    name = 'pustakalaya_apps.community'

    def ready(self):
        from . import signals

