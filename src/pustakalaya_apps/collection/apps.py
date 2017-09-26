from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CollectionConfig(AppConfig):
    name = 'pustakalaya_apps.collection'
    verbose_name = _("Categories")

    def ready(self):
        from . import signals
