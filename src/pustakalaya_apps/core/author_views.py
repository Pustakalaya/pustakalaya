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
    nepali_letters = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऋ', 'ए', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ',
                      'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'स',
                      'ष', 'ह']

    if request.method == "GET":
        query_letter = request.GET.get('letter', None)

        if not query_letter:
            authors = Biography.objects.all()
        else:
            authors = Biography.objects.filter(first_name__startswith=query_letter)

    return render(request, "core/author_list.html", {
        "letters": letters,
        "authors": authors,
        "nepali_letters": nepali_letters
    })
