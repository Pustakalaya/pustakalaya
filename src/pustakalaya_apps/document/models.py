#  document/models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _

from pustakalaya_apps.collection.models import Collection
from pustakalaya_apps.core.abstract_models import (
    AbstractItem,
    AbstractSeries,
    AbstractTimeStampModel
)
from pustakalaya_apps.core.models import (
    Publisher,
    Biography,
    Category,
    Keyword,
    Sponsor,
)
from .search import DocumentDoc


def __file_upload_path(instance, filepath):
    # Should return itemtype/year/month/filename
    # return instance.type
    # return document/pdf/year/month/filename
    pass


class Document(AbstractItem):
    """Book document type to store book type item
    Child class of AbstractItem
    """

    ITEM_INTERACTIVE_TYPE = (
        ("interactive", _("Interactive")),
        ("noninteractive", _("Non interactive")),
    )

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

    collection = models.ManyToManyField(
        Collection,
        verbose_name=_("Add to these collections"),
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

    document_interactivity = models.CharField(
        verbose_name=_("Interactive type"),
        max_length=15,
        choices=ITEM_INTERACTIVE_TYPE
    )

    # This field should be same on all other model to make searching easy in search engine.
    type = models.CharField(
        max_length=255, editable=False, default="document"
    )

    document_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_("Document Category")
    )

    document_total_page = models.PositiveIntegerField(
        verbose_name=_("Document pages")
    )

    document_author = models.ManyToManyField(
        Biography,
        verbose_name=_("Document Author"),
        related_name="authors"
    )

    document_editor = models.ManyToManyField(
        Biography,
        verbose_name=_("Document Editor"),
        related_name="editors"
    )

    document_illustrator = models.ManyToManyField(
        Biography,
        verbose_name=_("Document Illustrator"),
        related_name="illustrators"
    )

    document_identifier_type = models.CharField(
        _("Identifier type"),
        choices=(
            ("issn", _("ISSN")),
            ("ismn", _("ISMN")),
            ("govt doc", _("Gov't Doc")),
            ("uri", _("URI")),
            ("isbn", _("ISBN"))
        ),
        max_length=255  # TODO
    )

    publisher = models.ForeignKey(
        Publisher,
        verbose_name=_("Publisher name")
    )
    # Better to have plural name
    keywords = models.ManyToManyField(
        Keyword,
        verbose_name=_("Select list of keywords")
    )

    document_thumbnail = models.ImageField(
        upload_to="uploads/thumbnails/audio/%Y/%m/%d",
        max_length=255
    )

    sponsors = models.ManyToManyField(
        Sponsor,
        verbose_name=_("Sponsor"),

    )

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def doc(self):
        """Create and return document object"""
        obj = DocumentDoc(
            meta={'id': self.id},
            id=self.id,
            title=self.title,
            abstract=self.abstract,
            type=self.type,
            education_level=self.education_level,
            category=self.category,
            language=self.language,
            additional_note=self.additional_note,
            description=self.description,
            license_type=self.license_type,
            year_of_available=self.year_of_available,
            date_of_issue=self.date_of_issue,
            place_of_publication=self.place_of_publication,
            created_date=self.created_date,
            updated_date=self.updated_date,
            # Common fields in document, audio and video library
            publisher=self.publisher.publisher_name,
            sponsors=[sponsor.name for sponsor in self.sponsors.all()],  # Multi value # TODO some generators
            collections=[c.collection_name for c in self.collection.all()],  # ToDO generator
            keywords=[keyword.keyword for keyword in self.keywords.all()],

            # Document type specific
            document_thumbnail=self.document_thumbnail.name,
            document_identifier_type=self.document_identifier_type,
            document_total_page=self.document_total_page,
            document_category=self.document_category.category_name,
            document_file_type=self.document_file_type,
            document_interactivity=self.document_interactivity,
            document_type=self.document_type,
            document_authors=[
                author.getname for author in self.document_author.all()
                ],
            document_illustrators=[
                illustrator.getname for illustrator in self.document_illustrator.all()
                ],  # Multi value TODO generator
            document_editors=[
                editor.getname for editor in self.document_editor.all()
                ]  # Multi value

        )

        return obj

    def index(self):
        """index or update a document instance to elastic search index server"""
        self.doc().save()
        return self.doc().to_dict(include_meta=True)

    def delete_index(self):
        self.doc().delete()


class DocumentSeries(AbstractSeries):
    """BookSeries table inherited from AbstractSeries"""

    def __str__(self):
        return self.series_name


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
        upload_to="uploads/documents/%Y/%m/",
        max_length=255
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
