from django import forms
from pustakalaya_apps.document.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"
