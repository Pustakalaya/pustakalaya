from django import forms
from django.utils.translation import ugettext_lazy as _


class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label=_("Name"),
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'class': 'form-control',
            'placeholder': _("Your name")
        })
    )
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'class': 'form-control',
            'placeholder': _("Email")
        })
    )

    country = forms.CharField(
        label=_("Country"),
        required=False,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'off',
                'class': 'form-control',
                'placeholder': _("Your country")
            }

        )
    )
    address = forms.CharField(
        label=_("Address"),
        required=False,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'off',
                'class': 'form-control',
                'placeholder': _("Your Address")
            }

        )
    )
    suggestion = forms.CharField(
        label=_("Suggestion"),
        widget=forms.Textarea(
            attrs={
                'autocomplete': 'off',
                'class': 'form-control',
                'placeholder': _("Your Message"),
                'cols': 50,
                'rows': 5
            }

        )

    )

    def clean(self):
        cleaned_data = super(FeedBackForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        country = cleaned_data.get('country')
        address = cleaned_data.get('address')
        suggestion = cleaned_data.get('suggestion')

        if not name and not email and not country and not address and not suggestion:
            raise forms.ValidationError('You have to write something!')
