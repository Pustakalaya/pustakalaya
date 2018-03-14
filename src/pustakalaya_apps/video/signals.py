# video/signals.py
# Used in apps.py

from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver
from django.db import transaction

from .models import Video


@receiver(m2m_changed, sender=Video.keywords.through)
@receiver(m2m_changed, sender=Video.video_producers.through)
@receiver(m2m_changed, sender=Video.languages.through)
@receiver(m2m_changed, sender=Video.collections.through)
@receiver(m2m_changed, sender=Video.sponsors.through)
@receiver(post_save, sender=Video)
@transaction.atomic
def index_or_update_video(sender, instance, **kwargs):
    """Update or create an instance to index server."""
    if instance.license.license:
        instance.license_type = instance.license.license
    # TODO: use logging system
    #print("Instance", sender, instance)

    instance.index()


@receiver(pre_delete, sender=Video)
@transaction.atomic
def delete_video(sender, instance, **kwargs):
    """Delete an item from index server."""
    # TODO: Use logging system
    print("Delete index object")
    instance.delete_index()
