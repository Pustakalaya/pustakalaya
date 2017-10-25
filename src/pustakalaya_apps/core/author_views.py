from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Biography
from django.shortcuts import (
    HttpResponse,
    render,
)


def home(request):
    return render(request, "index.html", {})



class AuthorDetail(DetailView):
    model = Biography

    template_name = "core/author_detail.html"
