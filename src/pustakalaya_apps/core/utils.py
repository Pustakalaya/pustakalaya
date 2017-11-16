"""
Elastic search utils functions
"""

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def list_search_from_elastic(request, query_type="match", **kwargs):
    """
    Return a list of matching document when query value matches the field value.

    Usage: list_display(request, "mero katha", "title")

    Search the item in elastic search and return the list of items.
    :param request:
    :param name: name to search
    :param pk: primary key of a search string.
    :return: dict
    """
    # Context holder
    context = {}
    sort_order_type = "asc", "desc"
    sort_by_type = "title.raw", "updated_date"

    if request.method == "GET":
        # Default sort options
        sort_by = request.GET.get("sort_by") or "updated_date"
        sort_order = request.GET.get("sort_order") or "asc"

        if sort_order not in sort_order_type:
            sort_order = "asc"

        if sort_by not in sort_by_type:
            sort_by = "title.keyword"

    # Query to elastic search to grab all the items related to this collection name
    # And sort the result based on the sorting options.
    client = Elasticsearch()
    s = Search().using(client).query(query_type, **kwargs).sort({
        sort_by: {"order": sort_order}
    })



    # Pagination configuration before executing a query.
    paginator = Paginator(s, 50)

    page_no = request.GET.get('page')
    try:
        page = paginator.page(page_no)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    response = page.object_list.execute()



    context["response"] = response
    context["sort_order"] = sort_order
    context["sort_by"] = sort_by
    context["page_obj"] = page
    context["paginator"] = paginator

    return context
