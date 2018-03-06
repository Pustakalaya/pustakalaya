import string
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
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
            author_list = Biography.objects.all()
        else:
            author_list = Biography.objects.filter(first_name__startswith=query_letter)

        # Get the page no.
        page = request.GET.get('page', 1)

        # Paginate the results
        paginator = Paginator(author_list, 25)
        try:
            authors = paginator.page(page)
        except PageNotAnInteger:
            authors = paginator.page(1)
        except EmptyPage:
            authors = paginator.page(paginator.num_pages)

    return render(request, "core/author_list.html", {
        "letters": letters,
        "authors": authors,
        "nepali_letters": nepali_letters
    })


def author_books(request, author_name):
    from pustakalaya_apps.core.utils import list_search_from_elastic
    """
    Query all the books by this author from ES.
    :param request:
    :param author_name:
    :return:
    """
    author_name = " ".join(author_name.split("-"))
    print(author_name)
    # TODO: explicitly define the index name
    search_field = "author_list"
    search_value = author_name
    kwargs = {
        search_field: search_value
    }

    # Query to elastic search in keywords field having the value of search_value
    # Return response object.

    context = list_search_from_elastic(request, **kwargs)

    context["keyword"] = context
    context["author"] = author_name
    # Reuse the keyword template
    return render(request, "core/author_books.html", context)
