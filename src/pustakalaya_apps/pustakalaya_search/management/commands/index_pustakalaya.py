from django.core.management.base import BaseCommand

from pustakalaya_apps.audio.search import index_audio
from pustakalaya_apps.collection.search import index_collection
from pustakalaya_apps.document.search import index_document
from pustakalaya_apps.video.search import index_video


class Command(BaseCommand):
    help = "Index db to index server"

    def handle(self, *args, **options):
        try:
            index_collection()
            index_document()
            index_audio()
            index_video()
        except Exception as e:
            self.stdout.write(self.style.ERROR("Problem occurred", e))
