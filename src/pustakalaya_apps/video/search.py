from django.conf import settings
from elasticsearch.helpers import bulk
from elasticsearch_dsl import FacetedSearch, Q, TermsFacet, DateHistogramFacet
from elasticsearch_dsl import Text
from elasticsearch_dsl.connections import connections

from pustakalaya_apps.core.abstract_search import ItemDoc


class VideoDoc(ItemDoc):
    """Elastic search schema for video type"""
    # Video type specific

    # Common fields in document, audio and video library
    publisher = Text()
    sponsors = Text(multi=True),
    keywords = Text(multi=True)

    video_running_time = Text()
    thumbnail = Text()
    video_director = Text()
    video_series = Text()
    video_certificate_license = Text()
    video_genre = Text()

    class Meta:
        index = settings.ES_INDEX
        doc_type = "video"


def index_video():
    """
    Method that index all the video objects to search server
    Call by pustakalaya_search app index_pustakalaya management command
    """
    from .models import Video
    # Create an index and populate the mappings
    VideoDoc.init()
    # Get elastic search client
    es = connections.get_connection()
    # Index all community with nested collection
    print("Indexing videos...")
    bulk(client=es, actions=(b.bulk_index() for b in Video.objects.all().iterator() if b.published == "yes"))


class VideoSearch(FacetedSearch):
    doc_types = [VideoDoc]
    index = settings.ES_INDEX

    fields = ['title^5', 'abstract^3']

    facets = {
        'keywords': TermsFacet(field='keywords.keyword', size=5),
        'languages': TermsFacet(field='languages.keyword', size=10),
        'education_levels': TermsFacet(field='education_levels.keyword', size=10),
        'communities': TermsFacet(field='communities.keyword', size=10),
        'year_of_available': DateHistogramFacet(field='year_of_available', interval='month', min_doc_count=0),

        # 'months': DateHistogramFacet(
        #     field='created_date',
        #     interval='month',
        #     min_doc_count=0),
    }

    def query(self, search, query):
        if not query:
            return search
        # query in tags, title and body for query
        q = Q('multi_match', fields=['title', 'abstract'], query=query)
        # also find questions that have answers matching query
        # q |= Q(
        #     'has_child',
        #     type='answer',
        #     query=Q('match', body=query),
        #     inner_hits={
        #         'highlight': {
        #             "pre_tags": ["[[["],
        #             "post_tags": ["]]]"],
        #             'fields': {'body': {'fragment_size': 30}}
        #         },
        #         '_source': False,
        #         'size': 1
        #     }
        # )

        # take the rating field into account when sorting
        search = search.query(
            'function_score',
            query=q,
            # functions=[SF('field_value_factor', field='keywords')]
        )

        return search

    def highlight(self, search):
        return search
