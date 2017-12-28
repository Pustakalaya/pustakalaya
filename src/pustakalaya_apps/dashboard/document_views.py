from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from pustakalaya_apps.document.models import (
    DocumentFileUpload,
    Document
)
from .forms import (
    DocumentForm,
    DocumentFileUploadForm,
    DocumentFileUploadFormSet
)


class AddDocumentView(SuccessMessageMixin, CreateView):
    form_class = DocumentForm
    template_name = "dashboard/document/document_add.html/"
    model = Document
    success_url = reverse_lazy("dashboard:profile")



    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #
    #     form_class = self.get_form_class()
    #
    #     form = self.get_form(form_class)
    #
    #     document_file_upload_formset = DocumentFileUploadFormSet()
    #
    #     document_form = DocumentForm()
    #
    #     return self.render_to_response(
    #
    #         self.get_context_data(form=form, document_file_upload_form=document_file_upload_formset)
    #
    #     )
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     document_file_upload_formset = DocumentFileUploadFormSet(self.request.POST, self.request.FILES)
    #
    #     if (form.is_valid() and document_file_upload_formset.is_valid()):
    #         return self.form_valid(form, document_file_upload_formset)
    #
    #
    #
    #     return self.form_invalid(form, document_file_upload_formset)
    #
    # def form_valid(self, form, document_file_upload_formset):
    #     """
    #     Called if all forms are valid. Creates a Author instance along
    #     with associated books and then redirects to a success page.
    #     """
    #     for uploaded_file in document_file_upload_formset:
    #         self.object = form.save()
    #         uploaded_file.instance = self.object
    #         uploaded_file.document = self.object.pk
    #         uploaded_file.save()
    #
    #     return HttpResponseRedirect(self.get_success_url())
    #
    # def form_invalid(self, form, document_file_upload_formset):
    #     """
    #     Called if whether a form is invalid. Re-renders the context
    #     data with the data-filled forms and errors.
    #     """
    #     return self.render_to_response(
    #         self.get_context_data(form=form, document_file_upload_formset=document_file_upload_formset)
    #     )
    #
    # def get_context_data(self, **kwargs):
    #     """ Add formset and formhelper to the context_data. """
    #     context = super(AddDocumentView, self).get_context_data(**kwargs)
    #     document_form = DocumentForm()
    #
    #     if self.request.POST:
    #         context['document_file_upload_formset'] = DocumentFileUploadFormSet(self.request.POST, self.request.FILES)
    #         context['document_form'] = document_form
    #     else:
    #         context['document_file_upload_formset'] = DocumentFileUploadFormSet()
    #         context['document_form'] = document_form
    #
    #     return context





















    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        document_file_upload_formset = DocumentFileUploadFormSet()

        return self.render_to_response(
            self.get_context_data(
                form=form,
                document_file_upload_formset=document_file_upload_formset,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        document_file_upload_formset = DocumentFileUploadFormSet(self.request.POST, instance=self.object)

        if form.is_valid() and document_file_upload_formset.is_valid():

            self.object = form.save(commit=False)
            print(self.object.title)
            self.object.save()

            return
            return self.form_valid(form, document_file_upload_formset)
        else:
            return self.form_invalid(form, document_file_upload_formset)

    def form_valid(self, form, document_file_upload_formset):
        """
        Called if all forms are valid. Creates Assignment instance along with the
        associated AssignmentQuestion instances then redirects to success url
        Args:
            form: Assignment Form
            assignment_question_form: Assignment Question Form

        Returns: an HttpResponse to success url

        """
        self.object = form.save(commit=False)
        # pre-processing for Assignment instance here...
        self.object.save()

        # saving AssignmentQuestion Instances
        document_file_upload_formset = document_file_upload_formset.save(commit=False)
        for uploaded_file in document_file_upload_formset:
            #  change the AssignmentQuestion instance values here
            #  aq.some_field = some_value
            uploaded_file.document = self.object.pk
            uploaded_file.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, document_file_upload_formset):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.

        Args:
            form: Assignment Form
            assignment_question_form: Assignment Question Form
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  document_file_upload_formset=document_file_upload_formset
                                  )
        )






        # def clean(self, AddDocumentView):
        #     cleaned_data = super(AddDocumentView, self).clean()
        #     title = cleaned_data.get('title')
        #     collections = cleaned_data.get('collections')
        #     document_file_type = cleaned_data.get('document_file_type')
        #     languages = cleaned_data.get('languages')
        #     document_interactivity = cleaned_data.get('document_interactivity')
        #     publisher = cleaned_data.get('publisher')
        #     keywords = cleaned_data.get('keywords')
        #     document_series = cleaned_data.get('document_series')
        #     document_type = cleaned_data.get('document_type')
        #     license_type = cleaned_data.get('license_type')
        #
        #     if not title and not collections and not document_file_type and not languages and not document_interactivity and not publisher and not keywords and not document_series and not document_type and not license_type:
        #         raise cleaned_data.ValidationError('You have to write something!')

        # def get_context_data(self, **kwargs):
        #     context = super(AddDocumentView, self).get_context_data(**kwargs)
        #     if self.request.POST:
        #         file_upload_form = DocumentFileUploadForm(self.request.POST)
        #         if file_upload_form.is_valid():
        #             file_upload_form.save()
        #
        #         context['document_file_upload_form'] = DocumentFileUploadForm(self.request.POST)
        #     else:
        #         context['document_file_upload_form'] = DocumentFileUploadForm()
        #
        #     return context


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
