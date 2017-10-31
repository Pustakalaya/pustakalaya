"""
Elastic search utils functions
"""

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections


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
    s = Search().using(client).query(query_type, **kwargs).sort({
        sort_by: {"order": sort_order}
    })

    response = s.execute()

    context["response"] = response
    context["sort_order"] = sort_order
    context["sort_by"] = sort_by

    return context
