from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from elasticsearch_dsl.connections import connections

from .models import Document

@receiver(post_save, sender=Document)
def index_or_update_document(sender, instance, **kwargs):
    # Save or update index
    instance.index()


@receiver(pre_delete, sender=Document)
def delete_document(sender, instance, **kwargs):
    # Delete an index

    instance.delete_index()



