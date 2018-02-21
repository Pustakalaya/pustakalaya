from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import HttpResponseRedirect, render
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from pustakalaya_apps.document.models import Document

from django.shortcuts import redirect
from pustakalaya_apps.document.models import (
    DocumentFileUpload,
    Document
)
from .forms import (
    DocumentForm,
    DocumentFileUploadFormSet
)


class AddDocumentView(SuccessMessageMixin, CreateView):
    form_class = DocumentForm
    template_name = "dashboard/document/document_add.html/"
    model = Document
    success_url = "/dashboard"

    # the inline forms in `inlines`
    def get_context_data(self, **kwargs):
        ctx = super(AddDocumentView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx['form'] = DocumentForm(self.request.POST)
            ctx['inlines'] = DocumentFileUploadFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            ctx['form'] = DocumentForm()
            ctx['inlines'] = DocumentFileUploadFormSet()
        return ctx

    # 1. Validate Form.
    def form_valid(self, form):
        context = self.get_context_data()
        # form upload inlines
        inlines = context["inlines"]
        # form = context["form"]

        if form.is_valid() and inlines.is_valid():
            # Save the object. and its children.
            self.object = form.save(commit=False)
            # Make published to no, as admin will review and set to yes.
            self.object.published = "no"
            self.object.submitted_by = self.request.user
            self.object.save()
            form.save_m2m() # Save other m2m fields.
            # Here instance is Document.
            inlines.instance = self.object
            inlines.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    # Handle the form in case all the invalid form.
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def user_submission(request):
    # Grab all the list in pagination format.
    user = request.user
    documents = Document.objects.filter(submitted_by=user)
    return render(request, 'dashboard/document/user_submitted_books.html', {
        'items': documents
    })


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
