"""This module contains all the elastic search field type mapped to django"""

from elasticsearch_dsl import Object, Text, Date, DocType
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk

# collection has many items so collection field is repeated all over the item
# Reuse this field
collection_field = Object(
    properties={
        'collection_name': Text(),
        'collection_description': Text(),
    }
)


class CollectionDoc(DocType):
    """Collection DocType"""
    created_date = Date()
    updated_date = Date()
    collection_name = Text()
    collection_description = Text()
    community_name = Text()
    title = Text()
    

    class Meta:
        index = "pustakalaya"
        doc_type = "collection"


def index_collection():
    from .models import Collection
    # Create an index and populate the mappings
    CollectionDoc.init()
    # Get elastic search client
    es = connections.get_connection()
    # Index all community with nested collection
    # TODO: logging
    print("Indexing communities and collection")
    bulk(client=es, actions=(b.index() for b in Collection.objects.all().iterator()))
