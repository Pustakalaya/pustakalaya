from django.shortcuts import render
from .models import Document
from django.views.generic import DetailView
from .search import DocumentSearch
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView



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


class DocumentDetailView(HitCountDetailView): # Detail view is inherited from HitCountDetailView
    model = Document
    count_hit = True

    def get(self, request, **kwargs):
        self.object = self.get_object()
        hit_count = HitCount.objects.get_for_object(self.object)

        # next, you can attempt to count a hit and get the response
        # you need to pass it the request object as well
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        context = self.get_context_data(object=self.object)
        print("hit count is", hit_count_response)
        return self.render_to_response(context)

    template_name = "document/document_detail.html"
