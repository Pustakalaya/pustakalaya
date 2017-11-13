from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(
        _("First name"),
        max_length=50,

    )

    last_name = models.CharField(
        _("Last name"),
        max_length=50
    )
    phone_no = models.CharField(
        _("Phone no"),
        max_length=10

    )






