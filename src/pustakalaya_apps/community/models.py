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

    def doc(self):
        """return elastic search community type obj equivalent of give community instance
        >>> from pustakalaya_apps.community.models import Community
        >>> community = Community.objects.first()
        >>> community.doc()
        CommunityDoc(index='pustakalaya', id=UUID('8b9e610e-3248-483b-8963-4a53ec46ac84'))
        """

        # Community have many collections, collection document can be nested to community doc.
        # Nesting list of collection can be done in V2.
        # TODO: move doc object to parent abstract class.
        obj = CommunityDoc(
            meta={'id': self.id},
            id=self.id,
            created_date=self.created_date,
            updated_date=self.updated_date,
            community_name=self.community_name,
            community_description=self.community_description,
        )

        return obj


    @property
    def collections(self):
        return self.collection_set.order_by('-created_date')

    def index(self):
        """function to serialize a model"""
        self.doc().save()
        return self.doc().to_dict(include_meta=True)

    def delete_index(self):
        """Delete an item from index server"""
        try:
            self.doc().delete()
        except Exception as e:
            print(e) #TODO: Log exception to std err


    def __str__(self):
        return self.community_name


    class Meta:
        db_table = "community"
