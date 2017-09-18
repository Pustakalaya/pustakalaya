from django.db import models
from django.utils.translation import ugettext as _

from pustakalaya_apps.core.abstract_models import AbstractTimeStampModel
from .search import CommunityDoc


class Community(AbstractTimeStampModel):
    community_name = models.CharField(
        _("Community name"),
        max_length=255,
        unique=True
    )

    community_description = models.CharField(
        _("Community description"),
        max_length=255
    )

    @property
    def collections(self):
        return self.collection_set.order_by('-created_date')


    #for b in Community.objects.all().iterator()

    def index(self):
        """function to serailize a model"""
        obj = CommunityDoc(
            meta={'id': self.id},
            id=self.id,
            created_date=self.created_date,
            updated_date=self.updated_date,
            community_name=self.community_name,
            community_description=self.community_description,
            collections=[c.index() for c in self.collections.iterator()]
        )
        obj.save()
        return obj.to_dict(include_meta=True)

    def __str__(self):
        return self.community_name
