from django.shortcuts import render
from .models import Document
from django.views.generic import DetailView
from .search import DocumentSearch


def documents(request):
    documents = Document.objects.all()
    return render(request, 'document/documents.html', {'documents': documents})

    # search all video
    # bs = DocumentSearch()

    # search with query for document query
    # bs = DocumentSearch(query="document")

    # search with the query and selected filters
    # Filters are grabbed from the input forms.
    filters = {
        'keywords': "hamro"
    }

    bs = DocumentSearch(query="video", filters=filters)

    response = bs.execute()
    # for facets in response.facets:
    #     print(facets)
    # print(response.facets)


    # access hits and other attributes as usual
    print(response.hits.total, 'hits total')
    for hit in response:
        print(hit.meta.score, hit.title)
    #
    for (tag, count, selected) in response.facets.keywords:
        print(tag, ' (SELECTED):' if selected else ':', count)

    for (tag, count, selected) in response.facets.languages:
        print(tag, ' (SELECTED):' if selected else ':', count)

    for (month, count, selected) in response.facets.year_of_available:
        print(month.strftime('%B %Y'), ' (SELECTED):' if selected else ':', count)

    return HttpResponse("Hello world")



class DocumentDetailView(DetailView):
    model = Document
    template_name = "document/document_detail.html"
