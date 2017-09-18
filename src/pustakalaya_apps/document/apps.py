from django.apps import AppConfig


class DocumentConfig(AppConfig):
    name = 'pustakalaya_apps.document'
    verbose_name = "Add Document"

    def ready(self):
        from . import signals

