from __future__ import print_function
import os
from wand.image import Image, Color
from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import post_save, pre_delete, m2m_changed

from .models import Document, DocumentFileUpload


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


def convert_pdf(filename, output_path, resolution=150, instance=None):
    """ Convert a PDF into images.
        All the pages will give a single png file with format:
        {pdf_filename}-{page_number}.png
        The function removes the alpha channel from the image and
        replace it with a white background.
    """
    all_pages = Image(filename=filename, resolution=resolution)
    for i, page in enumerate(all_pages.sequence):
        with Image(page) as img:
            img.format = 'png'
            img.background_color = Color('white')
            img.alpha_channel = 'remove'
            image_filename = '{}.png'.format(i)
            image_filename = os.path.join(output_path, image_filename)
            img.save(filename=image_filename)
            print(image_filename)

    instance.total_pages = i+1 #
    # save the instance
    instance.save()
    print(instance.total_pages)

# TODO: run this signal in celery.
@receiver(post_save, sender=DocumentFileUpload)
@transaction.atomic
def pdfto_image(sender, instance, **kwargs):
    """
    Function to convert pdf to images and save in upload folder.
    :return:
    """

    # Grab the instance
    # Convert all of its pdf to images
    # Get all the converted images.

    # grab the file upload instance
    file_full_path = instance.upload.path
    dir_path, file_name = os.path.split(file_full_path)

    # Convert to pdf and save images
    print("Converting to images")
    print(instance.file_name)
    # If total page is greater than zero, don't convert to images, it is already converted
    if instance.total_pages <= 0:
        convert_pdf(file_full_path, dir_path, 150, instance=instance)
    print("Finish conversion")
