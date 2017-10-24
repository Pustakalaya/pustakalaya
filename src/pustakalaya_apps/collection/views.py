from django.shortcuts import render
from django.shortcuts import HttpResponse


def collection_detail(request, name, pk):
    return HttpResponse(name + "Hello" + pk)
