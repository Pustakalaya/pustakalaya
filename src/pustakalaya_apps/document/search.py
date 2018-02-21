from django.conf import settings
from elasticsearch.helpers import bulk
from elasticsearch_dsl import Integer, Text, Long
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import (
    FacetedSearch,
    TermsFacet,
    DateHistogramFacet,
    Q,
    SF
)

from pustakalaya_apps.core.abstract_search import ItemDoc


class DocumentDoc(ItemDoc):
    """Elastic search schema for document type"""
    # Document type specific


    thumbnail = Text()
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
    bulk(client=es, actions=(b.bulk_index() for b in Document.objects.all().iterator() if b.published == "yes"))


class DocumentSearch(FacetedSearch):
    doc_types = ["document"]
    index = settings.ES_INDEX

    fields = ['title^5', 'abstract^3']

    facets = {
        'keywords': TermsFacet(field='keywords.keyword', size=5),
        'languages': TermsFacet(field='languages.keyword', size=10),
        'education_levels': TermsFacet(field='education_levels.keyword', size=10),
        'communities': TermsFacet(field='communities.keyword', size=10),
        'year_of_available': DateHistogramFacet(field='year_of_available', interval='month', min_doc_count=0),
        'document_type': TermsFacet(field='document_type.keyword', size=10),
        'document_file_type': TermsFacet(field='document_file_type.keyword', size=10),
        'document_authors': TermsFacet(field='document_authors', size=10),
        'license_type': TermsFacet(field='license_type.keyword', size=10),
        'collections': TermsFacet(field='collections.keyword', size=10),

    }

    def query(self, search, query):
        if not query:
            return search
        # query in tags, title and body for query
        q = Q('multi_match', fields=['title', 'abstract'], query=query)


        # take the title field into account when sorting
        search = search.query(
            'function_score',
            query=q,
            functions=[SF('field_value_factor', field='title')]
        )

        return search

    def highlight(self, search):
        return search
