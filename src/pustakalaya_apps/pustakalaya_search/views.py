from django.shortcuts import render
from .search import PustakalayaSearch


def search(request):
    # Store search result in dict obj
    search_result = {}

    # Query string from user input
    query_string = " "

    # Filters dict object
    filters = {}

    if request.method == "POST":
        query_string = request.POST.get('q', " ")
        search_obj = PustakalayaSearch(query=query_string)
        response = search_obj.execute()
        search_result["total_result"] = response.hits.total

        if response is not None:
            search_result = {
                "total_found": response.hits.total,
                "hits": response.hits,
                "types": response.facets.type,
                "languages": response.facets.languages,
                "education_levels": response.facets.education_levels,
                "communities": response.facets.communities,
                "collection": response.facets.collections,
                "keywords": response.facets.keywords,
                "year_of_available": response.facets.year_of_available,
                "license_type": response.facets.license_type,
                "publication_year": response.facets.publication_year,
                "response": response,
            }

        else:
            search_result = {}

        return render(request, "pustakalaya_search/search_result.html", search_result)

    return render(request, "pustakalaya_search/search_page.html", search_result)
