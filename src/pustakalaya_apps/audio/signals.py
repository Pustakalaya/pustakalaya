from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from .models import Audio

@receiver(post_save, sender=Audio)
def index_or_update_audio(sender, instance, **kwargs):
    """
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    # Update or index audio doc type
    instance.index()


@receiver(pre_delete, sender=Audio)
def delete_audio(sender, instance, **kwargs):
    """
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    # Update or index audio doc type
    instance.delete_index()