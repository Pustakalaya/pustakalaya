from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


# Set the default environ module
# Use base settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "pustakalaya.settings.production")
app = Celery('pustakalaya')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    # TODO: log to log files.
    print('Request: {0!r}'.format(self.request))
