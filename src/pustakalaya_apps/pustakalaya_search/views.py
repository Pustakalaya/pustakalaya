import json
from django.shortcuts import render
from .search import PustakalayaSearch
from json import JSONDecodeError
from elasticsearch_dsl import Search
from django.conf import settings
from elasticsearch_dsl.connections import connections
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseRedirect


def search(request):
    # Store search result in dict obj
    search_result = {}

    # Query string from user input
    query_string = " "

    if request.method == "GET":
        # Grab query from form.

        query_string = request.GET.get('q')

        # To prevent empty search using url only
        if query_string == "":
            return HttpResponseRedirect("/")

        print("Query string from form is", query_string)

        # Get data ajax request
        try:
            filters = json.loads(request.GET.get("form-filter", {}))
        except (TypeError, JSONDecodeError):
            filters = {}

        # Search in elastic search
        search_obj = PustakalayaSearch(query=query_string, filters=filters)

        # Pagination configuration before executing a query.
        paginator = Paginator(search_obj, 12)

        page_no = request.GET.get('page')
        try:
            page = paginator.page(page_no)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        response = page.object_list.execute()

        search_result["response"] = response
        search_result["hits"] = response.hits
        search_result["type"] = response.facets.type
        search_result["languages"] = response.facets.languages
        search_result["education_levels"] = response.facets.education_levels
        search_result["communities"] = response.facets.communities
        search_result["collections"] = response.facets.collections
        search_result["publication_year"] = response.facets.publication_year
        search_result["keywords"] = response.facets.keywords
        search_result["year_of_available"] = response.facets.year_of_available
        search_result["license_type"] = response.facets.license_type
        search_result["q"] = query_string or ""
        search_result["time"] = response.took / float(1000)  # Convert time in msec
        search_result["page_obj"] = page
        search_result["paginator"] = paginator

        # Implement keywords filter.
        keyword_list = []
        for (keyword, count, selected) in response.facets.keywords:
            keyword = dict(keyword=(keyword), count=count, selected=selected)
            keyword_list.append(keyword)

        # Pass the keyword_list as js_keyword to consume by frontend apps like jquery.
        data = {
            "keywords": keyword_list,
        }

        search_result["keywords_js"] = json.dumps(data)

        #For collection filtering
        # #collection_list =
        # # Implement collection filter.
        # collection_list = []
        # for (collection, count, selected) in response.facets.collections:
        #     collection = dict(collection=(collection), count=count, selected=selected)
        #     collection_list.append(collection)
        #
        # # Pass the collection_list as js_collection to consume by frontend apps like jquery.
        # collection_data = {
        #     "collections": collection_list,
        # }
        #
        # search_result["collections_js"] = json.dumps(collection_data)


        #
        # for (type, count, selected) in response.facets.type:
        #     print(type, ' (SELECTED):' if selected else ':', count)
        #
        # for (language, count, selected) in response.facets.languages:
        #     print(language, ' (SELECTED):' if selected else ':', count)
        #
        # for (education_level, count, selected) in response.facets.education_levels:
        #     print(education_level, ' (SELECTED):' if selected else ':', count)
        #
        # for (community, count, selected) in response.facets.communities:
        #     print(community, ' (SELECTED):' if selected else ':', count)
        #
        # for (collection, count, selected) in response.facets.collections:
        #     print(collection, ' (SELECTED):' if selected else ':', count)
        #
        # for (keyword, count, selected) in response.facets.keywords:
        #     print(keyword, ' (SELECTED):' if selected else ':', count)
        #
        # for (month, count, selected) in response.facets.year_of_available:
        #     print(month.strftime('%B %Y'), ' (SELECTED):' if selected else ':', count)
        #
        # for (license_type, count, selected) in response.facets.license_type:
        #     print(license_type, ' (SELECTED):' if selected else ':', count)
        #
        # for (month, count, selected) in response.facets.publication_year:
        #     print(month.strftime('%B %Y'), ' (SELECTED):' if selected else ':', count)

        return render(request, "pustakalaya_search/search_result.html", search_result)


def completion(request):
    """
    Method to query the completion result.
    :param request:
    :return:
    """

    client = connections.get_connection()

    if request.method == "GET":
        text = request.GET.get('suggest_text') or " "
        response = client.search(
            index=settings.ES_INDEX,
            body={"_source": "suggest",
                  "suggest": {
                      "title_suggest": {
                          "prefix": text,
                          "completion": {
                              "field": "title_suggest"
                          }
                      }
                  }
                  })

        suggested_items = []

    for suggest_item in response["suggest"]["title_suggest"][0]["options"]:
        suggested_items.append(suggest_item)

    return JsonResponse(json.dumps(suggested_items), safe=False)


def browse(request, browse_by="all"):
    """
    Browse the urls based on querystring
    :param request: all, title, author
    :return: response
    """

    # browse_by options
    browse_by_options = "title", "author", "all"

    if request.method == "GET":
        if browse_by is "all" or not browse_by in browse_by_options:
            browse_by = ["title"]

        if browse_by == "author":
            # set browse_by options as
            browse_by = ["document_authors.keyword", "directors.keyword", "read_by.keyword"]

        client = connections.get_connection()

        s = Search(using=client, index=settings.ES_INDEX).query("match_all").sort(
            {"title.keyword": {"order": "asc"}}
        )
        response = s.execute()

        return render(request, "pustakalaya_search/browse.html", {
            "response": response,

        })
