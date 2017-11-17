"""
Dashboard forms.
"""
from django import forms
from pustakalaya_apps.pustakalaya_account.models import UserProfile



class ProfileForm(forms.ModelForm):
    """
    Model form for profile user
    """

    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "phone_no", "user.username"]
