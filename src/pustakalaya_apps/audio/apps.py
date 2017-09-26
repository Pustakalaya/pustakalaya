from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AudioConfig(AppConfig):
    from django.utils.translation import ugettext_lazy as _

    name = "pustakalaya_apps.audio"
    verbose_name = _("Audio")

    def ready(self):
        from . import signals
