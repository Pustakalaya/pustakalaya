from __future__ import print_function
import os
from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import post_save, pre_delete, m2m_changed
from .models import Document, DocumentFileUpload
from .tasks import convert_pdf




@receiver(m2m_changed, sender=Document.keywords.through)
@receiver(m2m_changed, sender=Document.document_authors.through)
@receiver(m2m_changed, sender=Document.education_levels.through)
@receiver(m2m_changed, sender=Document.document_illustrators.through)
@receiver(m2m_changed, sender=Document.document_editors.through)
@receiver(m2m_changed, sender=Document)
@transaction.atomic
def index_or_update_document(sender, instance, **kwargs):
    # Save or update index
    print("Working or not working")
    instance.index()


@receiver(pre_delete, sender=Document)
@transaction.atomic
def delete_document(sender, instance, **kwargs):
    # Delete an index
    instance.delete_index()


# TODO: run this signal in celery.
@receiver(post_save, sender=DocumentFileUpload)
def pdfto_image(sender, instance, **kwargs):
    """
    Convert pdf to images
    """

    # grab the file path
    file_full_path = instance.upload.path
    file_name = os.path.split(file_full_path)[1]

    if not file_name.lower().endswith('.pdf'):
        return


    if instance.total_pages <= 0: # Document is not converted yet send for conversion.
        convert_pdf.delay(file_full_path, instance_id=instance.pk)
