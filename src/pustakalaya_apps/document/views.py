from django.shortcuts import render
from django.http import HttpResponse


def documents(request):
    return HttpResponse("Hello world")


def document_detail(request, pk):
    return render(request, 'collection/collection_detail.html', {'msg':"He"})

