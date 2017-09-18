from django.conf import settings
from pustakalaya_apps.core.abstract_search import ItemDoc
from elasticsearch_dsl import Integer, Text, Long
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk

class VideoDoc(ItemDoc):
    """Elastic search schema for video type"""
    # Document type specific
    video_category = Text()
    video_running_time = Text()
    video_thumbnail = Text()
    video_director = Text()
    video_producers = Text(multi=True)
    video_series = Text(multi=True)
    video_certificate_license = Text()

    class Meta:
        index = settings.ES_INDEX
        doc_type = "video"


def index_video():
    from .models import Video
    # Create an index and populate the mappings
    VideoDoc.init()
    # Get elastic search client
    es = connections.get_connection()
    # Index all community with nested collection
    print("Indexing videos...")
    bulk(client=es, actions=(b.index() for b in Video.objects.all().iterator()))
