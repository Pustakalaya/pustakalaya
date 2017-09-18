from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Video


@receiver(post_save, sender=Video)
def index_or_update_video(sender, instance, **kwargs):
    """Update or create an instance to index server."""
    # TODO: use logging system
    print("Index video")
    instance.index()


@receiver(pre_delete, sender=Video)
def delete_video(sender, instance, **kwargs):
    """Delete an item from index server."""
    # TODO: Use logging system
    print("Delete index object")
    instance.delete_index()
