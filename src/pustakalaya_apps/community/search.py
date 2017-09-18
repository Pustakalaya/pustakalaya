from elasticsearch_dsl import Object, Text, DocType, Nested, Date
from elasticsearch.helpers import bulk
from elasticsearch_dsl.connections import connections
from django.conf import settings

# reuse this field in other module
community_field = Object(
    properties={
        'community_name': Text(),
        'community_description': Text()
    }
)


class CommunityDoc(DocType):
    """Community doctype class to store community document"""
    id = Text()
    created_date = Date()
    updated_date = Date()
    community_name = Text(),
    community_description = Text()

    class Meta:
        index = settings.ES_INDEX
        doc_type = "community"


def index_community():
    from .models import Community
    # Create an index and populate the mappings
    CommunityDoc.init()
    # Get elastic search client
    es = connections.get_connection()
    # Index all community with nested collection
    print("Indexing communities and collection")
    bulk(client=es, actions=(b.index() for b in Community.objects.all().iterator()))
