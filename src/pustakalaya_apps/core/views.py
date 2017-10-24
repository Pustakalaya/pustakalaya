from django.shortcuts import render
from django.shortcuts import (
    HttpResponse,
    render,
)


def home(request):
    return render(request, "index.html", {})
