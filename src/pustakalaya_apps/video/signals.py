# video/signals.py
# Used in apps.py

from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver

from .models import Video


@receiver(m2m_changed, sender=Video.keywords.through)
#@receiver(post_save, sender=Video)
def index_or_update_video(sender, instance, **kwargs):
    """Update or create an instance to index server."""
    # TODO: use logging system
    print("Instance", sender, instance)
    instance.index()


@receiver(pre_delete, sender=Video)
def delete_video(sender, instance, **kwargs):
    """Delete an item from index server."""
    # TODO: Use logging system
    print("Delete index object")
    instance.delete_index()

#m2m_changed.connect(index_or_update_video, sender=index_or_update_video)
