from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from .models import Collection


@receiver(post_save, sender=Collection)
def index_collection(sender, instance, **kwargs):
    """Update an instance to index server."""
    instance.index()
    print("Index Collection")


@receiver(pre_delete, sender=Collection)
def delete_collection(sender, instance, **kwargs):
    """Delete an item from index server."""
    instance.delete_index()
