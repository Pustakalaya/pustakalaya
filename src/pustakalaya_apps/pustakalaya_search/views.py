import json
from collections import OrderedDict
from django.shortcuts import render
from .search import PustakalayaSearch
from django.shortcuts import redirect
from json import JSONDecodeError


def search(request):
    # Store search result in dict obj
    search_result = {}

    # Query string from user input
    query_string = " "

    if request.method == "GET":
        # Grab query from form.
        query_string = request.GET.get('q')
        print("Query string from form is", query_string)

        # Get data ajax request
        try:
            filters = json.loads(request.GET.get("form-filter", {}))
            print("I got filters", filters)
        except (TypeError, JSONDecodeError):
            filters = {}
            print("I can't get filters")

        # Search in elastic search
        search_obj = PustakalayaSearch(query=query_string, filters=filters)

        response = search_obj.execute()

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
        search_result["time"] = response.took / float(1000) # Convert time in msec

        for (type, count, selected) in response.facets.type:
            print(type, ' (SELECTED):' if selected else ':', count)

        for (language, count, selected) in response.facets.languages:
            print(language, ' (SELECTED):' if selected else ':', count)

        for (education_level, count, selected) in response.facets.education_levels:
            print(education_level, ' (SELECTED):' if selected else ':', count)

        for (community, count, selected) in response.facets.communities:
            print(community, ' (SELECTED):' if selected else ':', count)

        for (collection, count, selected) in response.facets.collections:
            print(collection, ' (SELECTED):' if selected else ':', count)

        for (keyword, count, selected) in response.facets.keywords:
            print(keyword, ' (SELECTED):' if selected else ':', count)

        for (month, count, selected) in response.facets.year_of_available:
            print(month.strftime('%B %Y'), ' (SELECTED):' if selected else ':', count)

        for (license_type, count, selected) in response.facets.license_type:
            print(license_type, ' (SELECTED):' if selected else ':', count)

        for (month, count, selected) in response.facets.publication_year:
            print(month.strftime('%B %Y'), ' (SELECTED):' if selected else ':', count)

        return render(request, "pustakalaya_search/search_result.html", search_result)


def browse(request):
    """
    Browse the urls based on querystring
    :param request: all, title, author
    :return: response
    """

    if request.method == "GET":
        # Grab the browse by, sort by variables
        browse_by = request.GET.get('browse_by', "title") # Default is title
        return render(request, "pustakalaya_search/browse.html",{
            "browse_by":browse_by
        })
