import json
from django.shortcuts import render
from .models import Document
from django.http import HttpResponse
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView
from .models import DocumentFileUpload
from django.core.exceptions import ValidationError
#from pustakalaya_apps.review_system.forms import ReviewForm
from pustakalaya_apps.review_system.models import Review
from pustakalaya_apps.favourite_collection.models import Favourite



def documents(request):
    documents = 1 or Document.objects.all()
    return render(request, 'document/documents.html', {'documents': documents})

def flipBook(request, pk):

    return render(request, 'document/flip_book.html', {
        "book_id":pk
    })


class DocumentDetailView(HitCountDetailView):  # Detail view is inherited from HitCountDetailView
    model = Document
    count_hit = True

    def get(self, request, **kwargs):
        self.object = self.get_object()
        hit_count = HitCount.objects.get_for_object(self.object)


        # next, you can attempt to count a hit and get the response
        # you need to pass it the request object as well
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        context = self.get_context_data(object=self.object)
        data_review = Review.objects.filter(content_id=self.object.pk, content_type='document',published=True)

        #print("review_data= ",data_review)
        #for item in data_review:
        #    print("item comment ="+item.post+",publish status="+ str(item.published))
        favourite_data=""
        # favourite item data extractions
        if request.user.is_authenticated:
            favourite_data = Favourite.objects.filter(favourite_item_id=self.object.pk, favourite_item_type='document', user=request.user);

        #print("context= ",context['hitcount']['pk'])
        #print("context= ", context)
        #pkvalue = Document.collections.attname
        #print("pk value = ",pkvalue)
        context["data_review"]= data_review

        context["favourite_data"]= favourite_data

        print("favourite_data=",context["favourite_data"])
        print("context= ", context)
        #print("user in the console= ",context["favourite_data"][0].user)
        return self.render_to_response(context)

    template_name = "document/document_detail.html"


def document_page_view(request, pk):
    json_response = {}
    if request.method == "GET":
        try:
            document = DocumentFileUpload.objects.get(pk=pk)
            if document:
                json_response["file_name"] = document.file_name
                json_response["title"] = document.document.title
                json_response["total_page"] = document.total_pages
                json_response["page_urls"] = document.get_files()
        except (DocumentFileUpload.DoesNotExist, ValidationError):
            pass

    # Create json response
    print(json_response)
    json_response = json.dumps(json_response)
    return HttpResponse(json_response, content_type="application/json")
