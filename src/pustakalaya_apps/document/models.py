#  document/models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from pustakalaya_apps.core.abstract_models import AbstractItem
from pustakalaya_apps.core.abstract_models import AbstractBaseAuthor
from pustakalaya_apps.core.abstract_models import AbstractSeries
from pustakalaya_apps.core.abstract_models import AbstractTimeStampModel

from pustakalaya_apps.collection.models import Collection


class Document(AbstractItem):
    """Book document type to store book type item
    Child class of AbstractItem
    """

    DOCUMENT_TYPE = (
        ("book", _("Book")),
        ("working paper", _("Working paper")),
        ("thesis", _("Thesis")),
        ("journal paper", _("Journal paper")),
        ("technical report", _("Technical report")),
        ("article", _("Article")),

    )

    DOCUMENT_FILE_TYPE = (
        ("ppt", _("PPT")),
        ("doc", _("Doc")),
        ("docx", _("Docx")),
        ("pdf", _("PDF")),
        ("pdf", _("PDF")),
        ("xlsx", _("Excel")),
        ("epub", _("Epub")),
        ("rtf", _("Rtf")),
        ("mobi", _("Mobi")),
    )

    item_Collection = models.ManyToManyField(
        Collection,
        verbose_name=_("Add to these collections")
    )

    document_type = models.CharField(
        _("Document type"),
        max_length=40,  # TODO: Change to match the exact value.
        choices=DOCUMENT_TYPE
    )

    document_file_type = models.CharField(
        _("Document file type"),
        choices=DOCUMENT_FILE_TYPE,
        max_length=23
    )

    document_series = models.ForeignKey(
        "DocumentSeries",
        verbose_name=_("Document series"),
        on_delete=models.CASCADE
    )

    document_total_pages = models.PositiveIntegerField(
        verbose_name=_("Document pages")
    )

    document_author = models.ManyToManyField(
        "DocumentAuthor",
        verbose_name=_("Document Author")
    )
    document_editor = models.ManyToManyField(
        "DocumentEditor",
        verbose_name=_("Document Editor")
    )
    document_illustrator = models.ManyToManyField(
        "DocumentIllustrator",
        verbose_name=_("Document Illustrator")
    )

    class Meta:
        ordering = ('item_title',)


class DocumentSeries(AbstractSeries):
    """BookSeries table inherited from AbstractSeries"""

    def __str__(self):
        return self.series_name


class DocumentAuthor(AbstractBaseAuthor):
   pass


class DocumentEditor(AbstractBaseAuthor):
   pass


class DocumentIllustrator(AbstractBaseAuthor):
   pass


class DocumentFileUpload(AbstractTimeStampModel):
    """Class to upload the multiple document objects"""

    file_name = models.CharField(
        _("File name"),
        max_length=255,
    )
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE
    )


    upload = models.FileField(
        upload_to="uploads/%Y/%m/%d",
        max_length=100
    )

    def __str__(self):
        return self.file_name



class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title