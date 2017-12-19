from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from pustakalaya_apps.pustakalaya_account.models import UserProfile
from pustakalaya_apps.document.models import Document
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
    fields =  (
        "first_name",
        "last_name",
        "phone_no",
    )
    template_name = 'dashboard/profile/profile.html'


class AddDocument(CreateView):
    model = Document
    fields = ['title','collections', 'document_file_type','languages','document_interactivity','publisher','keywords','document_series','document_type','license_type']
    template_name = "dashboard/document/document_add.html/"
    success_url = reverse_lazy("dashboard:profile")

    def clean(self, AddDocument):
        cleaned_data = super(AddDocument, self).clean()
        title = cleaned_data.get('title')
        collections = cleaned_data.get('collections')
        document_file_type = cleaned_data.get('document_file_type')
        languages = cleaned_data.get('languages')
        document_interactivity = cleaned_data.get('document_interactivity')
        publisher = cleaned_data.get('publisher')
        keywords = cleaned_data.get('keywords')
        document_series = cleaned_data.get('document_series')
        document_type = cleaned_data.get('document_type')
        license_type = cleaned_data.get('license_type')

        if not title and not collections and not document_file_type and not languages and not document_interactivity and not publisher and not keywords and not document_series and not document_type and not license_type:
            raise cleaned_data.ValidationError('You have to write something!')




