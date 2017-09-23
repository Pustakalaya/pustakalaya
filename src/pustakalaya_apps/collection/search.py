"""This module contains all the elastic search field type mapped to django"""

from elasticsearch_dsl import Object, Text, DocType

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
    created_date = Text()
    updated_date = Text()
    collection_name = Text()
    collection_description = Text()
    community_name = Text()

    class Meta:
        index = "pustakalaya"
        doc_type = "collection"
