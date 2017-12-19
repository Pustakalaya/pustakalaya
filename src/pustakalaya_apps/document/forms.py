from django import forms
from pustakalaya_apps.document.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'collections', 'document_file_type', 'languages', 'document_interactivity', 'publisher',
                  'keywords', 'document_series', 'document_type', 'license_type']


