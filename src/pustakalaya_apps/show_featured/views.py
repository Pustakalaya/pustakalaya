from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.shortcuts import HttpResponseRedirect
from pustakalaya_apps.document.models import Document
# Create your views here.


def show_all_featured_item(request):

    item_list = Document.objects.filter(featured="yes")

    print("item list = ",item_list)
    print("count = ",len(item_list))
    #print("item list = ", item_list[0].document_authors)
    paginator = Paginator(item_list, 24)
    page = request.GET.get('page')
    try:
        doc = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        doc = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 7777), deliver last page of results.
        doc = paginator.page(paginator.num_pages)

    print("featured doc = ",doc)

    return render(request, "show_featured/all_featured_item.html", {
        'favourite_documents':doc
    })


