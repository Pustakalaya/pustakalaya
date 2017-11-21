from django.conf import settings
from pustakalaya_apps.audio.search import AudioDoc
from pustakalaya_apps.video.search import VideoDoc
from pustakalaya_apps.document.search import DocumentDoc
from elasticsearch_dsl import (
    FacetedSearch,
    TermsFacet,
    DateHistogramFacet,
    SF,
    Q
)


class PustakalayaSearch(FacetedSearch):
    doc_types = [DocumentDoc, VideoDoc, AudioDoc]
    index = settings.ES_INDEX
    # Boost values
    fields = [
        'title^10',
        'keywords',
        'abstract',
        'description',
        'collections',
        'communities',
        'author_list'

    ]

    facets = {
        'type': TermsFacet(field='type.keyword', size=10),
        'languages': TermsFacet(field='languages.keyword', size=10),
        'education_levels': TermsFacet(field='education_levels.keyword', size=10),
        'communities': TermsFacet(field='communities.keyword', size=10),
        'collections': TermsFacet(field='collections.keyword', size=10),
        'keywords': TermsFacet(field='keywords.keyword', size=5),
        'year_of_available': DateHistogramFacet(field='year_of_available', interval='month', min_doc_count=0),
        'license_type': TermsFacet(field='license_type.keyword', size=10),
        'publication_year': DateHistogramFacet(field='year_of_available', interval='month', min_doc_count=0),

    }
