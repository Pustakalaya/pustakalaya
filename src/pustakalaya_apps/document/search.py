from django.conf import settings
from elasticsearch.helpers import bulk
from elasticsearch_dsl import Integer, Text, Long
from elasticsearch_dsl.connections import connections

from pustakalaya_apps.core.abstract_search import ItemDoc


class DocumentDoc(ItemDoc):
    """Elastic search schema for document type"""
    # Document type specific


    document_thumbnail = Text()
    document_total_page = Long()
    document_file_type = Text()
    document_type = Text()
    document_authors = Text(multi=True)
    document_illustrators = Text(multi=True)  # Multi value TODO generator
    document_editors = Text(multi=True)
    document_interactivity = Text()

    class Meta:
        index = settings.ES_INDEX
        doc_type = "document"


def index_document():
    from .models import Document
    # Create an index and populate the mappings
    DocumentDoc.init()
    # Get elastic search client
    es = connections.get_connection()
    # Index all community with nested collection
    print("Indexing Document data type...")
    bulk(client=es, actions=(b.bulk_index() for b in Document.objects.all().iterator()))
