from django.shortcuts import render
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections
from pustakalaya_apps.core.utils import list_search_from_elastic




def keyword_detail(request, keyword):
    search_string = " ".join(keyword.split("-"))
    # TODO: explicitly define the index name
    search_field = "keywords"
    search_value = search_string
    kwargs = {search_field:search_value}

    # Query to elastic search in keywords field having the value of search_value
    # Return response object.

    context = list_search_from_elastic(request, **kwargs)
    #
    # context["response"] = response
    context["keyword"] = keyword

    # Implement pagination


    return render(request, "core/keyword_detail.html", context)


