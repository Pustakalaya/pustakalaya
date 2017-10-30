from django.shortcuts import render
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


def keyword_detail(request, keyword):
    keyword = " ".join(keyword.split("-"))
    client = Elasticsearch()
    # TODO: explicitly define the index name
    s = Search().using(client).query("match", keywords=keyword)
    response = s.execute()
    context = {}

    context["response"] = response
    context["keyword"] = keyword

    return render(request, "core/keyword_detail.html", context)

