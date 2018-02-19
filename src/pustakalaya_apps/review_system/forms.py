from django import forms


class ReviewForm(forms.Form):
    input = forms.CharField(
        label='Your review ',
        max_length=100,
        widget=forms.TextInput(
            attrs={
            'class': 'form-control',
            'name': 'input',
            'placeholder': 'your review'
            }))
