from pustakalaya_apps.document.models import Document
from django.shortcuts import (
    render,
)


def home(request):
    """view that serve homepage"""
    featured_books = Document.featured_objects.all()
    context = {}
    context["featured_books"] = featured_books
    return render(request, "index.html", context)
