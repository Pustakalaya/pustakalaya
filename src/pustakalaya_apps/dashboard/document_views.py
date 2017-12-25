from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from pustakalaya_apps.document.models import Document
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import DocumentFileUploadForm

class AddDocumentView(CreateView):
    model = Document
    fields = [
                'title',
                'collections',
                'document_file_type',
                'languages',
                'document_interactivity',
                'publisher',
                'keywords',
                'document_series',
                'document_type',
                'license_type'
            ]

    template_name = "dashboard/document/document_add.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, AddDocumentView):
        cleaned_data = super(AddDocumentView, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        document_file_type = cleaned_data.get('document_file_type')
        languages = cleaned_data.get('languages')
        document_interactivity = cleaned_data.get('document_interactivity')
        publisher = cleaned_data.get('publisher')
        keywords = cleaned_data.get('keywords')
        document_series = cleaned_data.get('document_series')
        document_type = cleaned_data.get('document_type')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not document_file_type and not languages and not document_interactivity and not publisher and not keywords and not document_series and not document_type and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')

    def get_context_data(self, **kwargs):
        context = super(AddDocumentView, self).get_context_data(**kwargs)
        if self.request.POST:
            file_upload_form = DocumentFileUploadForm(self.request.POST)
            if file_upload_form.is_valid():
                file_upload_form.save()

            context['document_file_upload_form'] = DocumentFileUploadForm(self.request.POST)
        else:
            context['document_file_upload_form'] = DocumentFileUploadForm()

        return context


class UpdateDocumentView(SuccessMessageMixin, UpdateView):
    model = Document
    fields = [
                'title',
                'collections',
                'document_file_type',
                'languages',
                'document_interactivity',
                'publisher',
                'keywords',
                'document_series',
                'document_type',
                'license_type'
    ]

    template_name = "dashboard/document/document_edit.html/"
    success_url = 'dashboard/document/document_edit.html/'
    success_message = "was update successfully !!"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, UpdateDocument):
        cleaned_data = super(UpdateDocument, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        document_file_type = cleaned_data.get('document_file_type')
        languages = cleaned_data.get('languages')
        document_interactivity = cleaned_data.get('document_interactivity')
        publisher = cleaned_data.get('publisher')
        keywords = cleaned_data.get('keywords')
        document_series = cleaned_data.get('document_series')
        document_type = cleaned_data.get('document_type')
        license_type = cleaned_data.get('license_type')
        form_class = DocumentFileUploadForm()

        if not title and not collections and not document_file_type and not languages and not document_interactivity and not publisher and not keywords and not document_series and not document_type and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')


class DeleteDocumentView(SuccessMessageMixin, DeleteView):
    model = Document
    fields = [
                'title',
                'collections',
                'document_file_type',
                'languages',
                'document_interactivity',
                'publisher',
                'keywords',
                'document_series',
                'document_type',
                'license_type'
    ]

    template_name = "dashboard/document/document_delete.html/"
    success_url = '/'
    success_message = "was deleted successfully"
