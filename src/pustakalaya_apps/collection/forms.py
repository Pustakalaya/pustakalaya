from django import forms
from .models import Collection

class CollectionForm(forms.ModelForm):
    """
    Collection model form
    """

    class Meta:
        model = Collection
