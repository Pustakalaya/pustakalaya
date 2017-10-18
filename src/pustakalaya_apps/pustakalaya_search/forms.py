from django import forms


class PustakalayaSearchForm(forms.Form):
    search_text = forms.CharField(
        max_length=100,
    )
