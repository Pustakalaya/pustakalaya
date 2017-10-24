from django.shortcuts import render
from elasticsearch import Elasticsearch
from django.conf import settings
from elasticsearch_dsl import Search
from django.http import HttpResponse
from .models import Collection
from pustakalaya_apps.pustakalaya_search.search import PustakalayaSearch
from pustakalaya_apps.document.search import DocumentDoc


def community_detail(request, community_name):
    """Community detail page"""

    # Context data
    context = {}

    community_name = " ".join(community_name.split("-"))

    # Query all the collection that contains this community_name from ORM
    collections = Collection.objects.filter(community_name=community_name)

    collection_list = []

    all_total = 0

    for collection in collections:
        # Query the total no of object in this collection using elastic instance.
        total_documents = collection.document_set.count()
        total_audio = collection.audio_set.count()
        total_video = collection.video_set.count()
        total_count = total_documents + total_audio + total_video
        pk = collection.pk
        all_total += total_count

        # Create a list to that contain collection_name and total count
        collection_list.append({
            "collection_name": collection.collection_name,
            "total_count": total_count,
            "pk": pk,
        })

    # Sort list to display in alphabetical order.
    context["collection_list"] = collection_list

    return render(request, "collection/community_detail.html", context)
