from django.shortcuts import render

from .models import Collection
from elasticsearch import Elasticsearch
from django.conf import settings
from elasticsearch_dsl import Search
from pustakalaya_apps.pustakalaya_search.search import PustakalayaSearch
from pustakalaya_apps.document.search import DocumentDoc


def collection_detail(request, name, pk):
    print("Collection", name)
    collection_name = " ".join(name.split("-"))
    print("COllection name", collection_name)
    collection = Collection.objects.get(pk=pk)
    context = {}

    # Grab all the items for ES which belongs to this collection.
    # Dispatch to the detail page.
    client = Elasticsearch()
    s = Search().using(client).query("match", collections=name)

    response = s.execute()
    print(response.to_dict())


    context["response"] = response
    context["collection_name"] = collection_name
    context["collection_pk"] = pk
    context["community_name"] = collection.community_name


    return render(request, "collection/collection_detail.html", context)
