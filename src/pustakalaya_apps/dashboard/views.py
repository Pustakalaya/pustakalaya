from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from pustakalaya_apps.pustakalaya_account.models import UserProfile
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required()
def dashboard(request):
    return render(request, "dashboard/dashboard_base.html")


def profile(request):
    """
    Render the user profile template
    :param request:
    :return:
    """
    return render(request, 'dashboard/profile.html', {
        "user": request.user
    })


def profile_edit(request):
    pass


class ProfileEdit(UpdateView):
    model = UserProfile
    fields = (
        "first_name",
        "last_name",
        "phone_no",
    )
    template_name = 'dashboard/profile/profile.html'








