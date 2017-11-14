from django import forms
from .models import UserProfile

class SignupForm(forms.ModelForm):
    """
    SignupForm class
    """

    class Meta:
        model = UserProfile

        fields = (
            "first_name",
            "last_name",
            "phone_no",
        )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        # Save the user
        user.save()

        # Save the profile of a user.
        profile = UserProfile()
        profile.user = user
        profile.phone_no = self.cleaned_data['phone_no']
        # save user profile.
        profile.save()


# class PustakalayaSignUpform(sf):
#     def __init__(self, *args, **kwargs):
#         super(PustakalayaSignUpform, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = UserProfile
#         fields = (
#             "first_name",
#             "last_name",
#             "phone_no",
#         )
#
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#
#         # Save the user
#         user.save()
#
#         # Save the profile of a user.
#         profile = UserProfile()
#         profile.user = user
#         profile.phone_no = self.cleaned_data['phone_no']
#         # save user profile.
#         # profile.save()
