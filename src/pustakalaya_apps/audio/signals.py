from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.db import transaction
from .models import Audio


@receiver(post_save, sender=Audio.keywords.through)
@receiver(post_save, sender=Audio.collections.through)
@receiver(post_save, sender=Audio.languages.through)
@receiver(post_save, sender=Audio.education_levels.through)
@receiver(post_save, sender=Audio)
@transaction.atomic
def index_or_update_audio(sender, instance, **kwargs):
    """
    Index or update audio instance to es server
    """
    instance.license_type = instance.license.license
    # Update or index audio doc type
    instance.index()


@receiver(pre_delete, sender=Audio)
@transaction.atomic
def delete_audio(sender, instance, **kwargs):
    """
    Delete audio instance from es server
    """
    # Update or index audio doc type
    # TODO: implement logging
    # TODO: log this event
    instance.delete_index()
