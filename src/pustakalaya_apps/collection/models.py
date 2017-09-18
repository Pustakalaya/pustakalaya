from django.db import models
from django.utils.translation import ugettext as _
from pustakalaya_apps.core.abstract_models import AbstractTimeStampModel
from pustakalaya_apps.community.models import Community
from .search import CollectionDoc


class Collection(AbstractTimeStampModel):

    collection_name = models.CharField(
        _("Collection name"),
        max_length=255
    )

    collection_description = models.CharField(
        _("Collection description"),
        max_length=255
    )

    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
        verbose_name=_("Community")
    )

    def index(self):
        """function to serailize a model"""
        obj = CollectionDoc(
            meta={'id': self.id},
            id=self.pk,
            created_date=self.created_date,
            updated_date=self.updated_date,
            collection_name=self.collection_name,
            collection_description=self.collection_description
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    def __str__(self):
        return self.collection_name


    class Meta:
        db_table = "collection"



