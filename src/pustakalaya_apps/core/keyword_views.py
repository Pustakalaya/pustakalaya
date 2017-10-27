from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Keyword
from .models import Biography
from django.shortcuts import (
    HttpResponse,
    render,
)


def keyword_detail(request):
    return render(request, "index.html", {})


class KeywordDetail(DetailView):
    model = Keyword


    template_name = "core/keyword_detail.html"
