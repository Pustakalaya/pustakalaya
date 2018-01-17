from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext as _
from elasticsearch.exceptions import ConnectionError, NotFoundError
from elasticsearch_dsl.connections import connections

from pustakalaya_apps.core.abstract_models import AbstractTimeStampModel
from .search import CollectionDoc


class Collection(AbstractTimeStampModel):
    """
    Database model that hold information about a category.
    Collection are also called the sub-category. For instance Literature is a category
    while `english literature` is a sub-category
    """
    CATEGORY = (
        ("literatures and arts", _("Literature and arts")),
        ("course materials", _("Course materials")),
        ("teaching materials", _("Teaching materials")),
        ("reference materials", _("Reference materials")),
        ("other educational materials", _("Other educational materials")),
        ("newspaper and magazines", _("newspaper and magazines")),
    )

    community_name = models.CharField(
        choices=CATEGORY,
        max_length=255,
        verbose_name=_("Community")
    )

    collection_name = models.CharField(
        _("Collection name"),
        max_length=255,
        unique=True
    )

    collection_description = models.TextField(
        _("Collection description"),
    )

    def save(self, *args, **kwargs):
        # Check the index server, If index server is down, reject the save
        if not connections.get_connection().ping():
            raise ValidationError("Cannot connect to elastic server")
            return

        super(Collection, self).save(*args, **kwargs)

    def doc(self):
        """Create collection document type"""
        obj = CollectionDoc(
            meta={'id': self.id},
            id=self.id,
            created_date=self.created_date,
            updated_date=self.updated_date,
            collection_name=self.collection_name,
            collection_description=self.collection_description,
            community_name=self.community_name
        )

        return obj

    def index(self):
        """method to serailize a model"""
        self.doc().save()
        return self.doc().to_dict(include_meta=True)

    def delete_index(self):
        try:
            self.doc().delete()
        except (ConnectionError, NotFoundError):
            pass

    def __str__(self):
        return self.collection_name

    class Meta:
        db_table = "collection"
