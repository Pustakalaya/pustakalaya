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

    nepali_letters = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऋ', 'ए','क','ख','ग' ,'घ' ,'ङ', 'च', 'छ', 'ज', 'झ', 'ञ','ट', 'ठ', 'ड', 'ढ', 'ण','त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'स', 'ष', 'ह']

    authors = Biography.objects.all()
    context = {}
    context["letters"] = letters
    context["authors"] = authors
    context["nepali_letter"] = nepali_letters

    return render(request, "core/author_list.html", context)
