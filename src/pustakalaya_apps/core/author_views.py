import string
from django.views.generic.detail import DetailView
from .models import Biography
from django.shortcuts import (
    render,
)


def home(request):
    return render(request, "index.html", {})


class AuthorDetail(DetailView):
    model = Biography

    template_name = "core/author_detail.html"


def author_list(request):
    # hold some data.
    letters = string.ascii_lowercase
    nepali_letters = [""]
    authors = Biography.objects.all()
    context = {}
    context["letters"] = letters
    context["authors"] = authors
    return render(request, "core/author_list.html", context)
