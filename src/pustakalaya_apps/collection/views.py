from django.shortcuts import render

from .models import Collection
from elasticsearch import Elasticsearch
from django.conf import settings
from elasticsearch_dsl import Search
from pustakalaya_apps.pustakalaya_search.search import PustakalayaSearch
from pustakalaya_apps.document.search import DocumentDoc


def collection_detail(request, name, pk):
    """
    Render collection detail
    :param request:
    :param name: collection_name
    :param pk: primary key of a collection
    :return: Response Obj
    """
    # Context holder
    context = {}
    sort_order_type = "asc", "desc"
    sort_by_type = "title.keyword", "updated_date"

    if request.method == "GET":
        # Default sort options
        sort_by = request.GET.get("sort_by") or "title.keyword"
        sort_order = request.GET.get("sort_order") or "asc"

        if sort_order not in sort_order_type:
            sort_order = "asc"

        if sort_by not in sort_by_type:
            sort_by = "title.keyword"

    # Query to elastic search to grab all the items related to this collection name
    # And sort the result based on the sorting options.
    client = Elasticsearch()
    s = Search().using(client).query("match", collections=name).sort({
            sort_by: {"order": sort_order}
        })

    response = s.execute()

    collection_name = " ".join(name.split("-"))
    collection = Collection.objects.get(pk=pk)

    context["response"] = response
    context["collection_name"] = collection_name
    context["collection_pk"] = pk
    context["community_name"] = collection.community_name
    context["sort_order"] = sort_order
    context["sort_by"] = sort_by

    return render(request, "collection/collection_detail.html", context)
