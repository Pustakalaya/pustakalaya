from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import post_save, pre_delete, m2m_changed

from .models import Document


@receiver(m2m_changed, sender=Document.keywords.through)
@receiver(m2m_changed, sender=Document.document_authors.through)
@receiver(m2m_changed, sender=Document.education_levels.through)
@receiver(m2m_changed, sender=Document.document_illustrators.through)
@receiver(m2m_changed, sender=Document.document_editors.through)
@receiver(m2m_changed, sender=Document)
@transaction.atomic
def index_or_update_document(sender, instance, **kwargs):
    # Save or update index
    instance.index()


@receiver(pre_delete, sender=Document)
@transaction.atomic
def delete_document(sender, instance, **kwargs):
    # Delete an index

    instance.delete_index()
