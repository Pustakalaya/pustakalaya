from django.shortcuts import render
from django.shortcuts import (
    HttpResponse,
    render,
)


def hello(request):
    return render(request, "base.html", {})
