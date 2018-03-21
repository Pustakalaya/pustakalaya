import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from collections import OrderedDict
from django.shortcuts import render
from .search import PustakalayaSearch
from django.shortcuts import redirect
from json import JSONDecodeError
from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch
from django.conf import settings
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Q
from pustakalaya_apps.core.utils import list_search_from_elastic
from pustakalaya_apps.document.search import DocumentDoc


def browse(request):
    """
    Browse the urls based on querystring
    :param request: all, title, author
    :return: response
    """

    # browse_by options
    browse_by_type = "title", "author", "all"

    # Sorting options
    sort_order_type = "asc", "desc"
    sort_by_type = "title.keyword", "updated_date"

    if request.method == "GET":
        # Grab the browsing field.
        browse_by = request.GET.get("browse_by", "title.keyword")  # default browsing is by title.

        # Grab the sort order field.
        sort_by = request.GET.get("sort_by") or "title.keyword"
        sort_order = request.GET.get("sort_order") or "asc"

        if sort_order not in sort_order_type:
            sort_order = "asc"

        if sort_by not in sort_by_type:
            sort_by = "title.keyword"

        if browse_by == "author":
            # sort by authors keyword
            sort_by = sort_by or "author_list.keyword"

        if browse_by == "all" or browse_by == "title" or browse_by not in browse_by_type:
            sort_by = sort_by or "title.keyword"

        # Create the query parameter
        query = [
            {sort_by: {"order": sort_order}},
        ]


        client = connections.get_connection()

        s = Search(using=client, index="pustakalaya", doc_type=DocumentDoc).query("match_all").sort(
            *query
        )

        response = s.execute()

        # Pagination configuration before executing a query.
        paginator = Paginator(response, 25)
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            books = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 7777), deliver last page of results.
            books = paginator.page(paginator.num_pages)

        return render(request, "pustakalaya_search/browse.html", {
            "response": books,
            "sort_by": sort_by,
            "sort_order": sort_order,
            "count":len(response)

        })
