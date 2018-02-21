from django.conf import settings
from elasticsearch.helpers import bulk
from elasticsearch_dsl import Text
from elasticsearch_dsl.connections import connections

from pustakalaya_apps.core.abstract_search import ItemDoc


class AudioDoc(ItemDoc):
    """Elastic search schema for video type"""
    # Document type specific
    audio_types = Text(multi=True)
    audio_running_time = Text()
    audio_running_time = Text()
    audio_read_by = Text()
    audio_genre = Text()
    thumbnail = Text()

    class Meta:
        index = settings.ES_INDEX
        doc_type = "audio"


def index_audio():
    from .models import Audio
    # Create an index and populate the mappings
    AudioDoc.init()
    # Get elastic search client
    es = connections.get_connection()
    # Index all community with nested collection
    print("Indexing Audios...")
    bulk(client=es, actions=(b.bulk_index() for b in Audio.objects.all().iterator() if b.published == "yes"))
