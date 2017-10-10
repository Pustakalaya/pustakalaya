from django.conf import settings
from pustakalaya_apps.core.abstract_search import ItemDoc
from elasticsearch_dsl import Integer, Text, Long, Date
from elasticsearch_dsl.connections import connections
from elasticsearch.helpers import bulk


class VideoDoc(ItemDoc):
    """Elastic search schema for video type"""
    # Video type specific

    # Common fields in document, audio and video library
    publisher = Text()
    sponsors = Text(multi=True),
    keywords = Text(multi=True)

    video_running_time = Text()
    video_thumbnail = Text()
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
    bulk(client=es, actions=(b.bulk_index() for b in Video.objects.all().iterator()))
