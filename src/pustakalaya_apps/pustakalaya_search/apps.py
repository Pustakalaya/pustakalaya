from django.apps import AppConfig
from django.conf import settings

from elasticsearch_dsl.connections import connections


class PustakalayaSearchConfig(AppConfig):
    name = 'pustakalaya_search'

    def ready(self):
        x = connections.configure(**settings.ES_CONNECTIONS)
        print(x, "hello")
