from django.apps import AppConfig


class CollectionConfig(AppConfig):
    name = 'pustakalaya_apps.collection'

    def ready(self):
        from . import signals
