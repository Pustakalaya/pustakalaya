from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DocumentConfig(AppConfig):
    name = 'pustakalaya_apps.document'
    verbose_name = _("Document")

    def ready(self):
        from . import signals
