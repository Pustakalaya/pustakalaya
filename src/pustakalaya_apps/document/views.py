from django.shortcuts import render
from .models import Document
from django.views.generic import DetailView


def documents(request):
    documents = Document.objects.all()
    return render(request, 'document/documents.html', {'documents': documents})


class DocumentDetailView(DetailView):
    model = Document
    template_name = "document/document_detail.html"

