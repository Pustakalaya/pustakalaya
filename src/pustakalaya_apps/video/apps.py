from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class VideoConfig(AppConfig):
    name = 'pustakalaya_apps.video'
    verbose_name = _("Video")

    def ready(self):
        from . import signals
