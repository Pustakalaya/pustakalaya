from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Community


@receiver(post_save, sender=Community)
def index_community(sender, instance, **kwargs):
    """Update an instance to index server."""
    print("Index community")
    instance.index()


@receiver(pre_delete, sender=Community)
def delete_community(sender, instance, **kwargs):
    """Delete an item from index server."""
    instance.delete_index()
