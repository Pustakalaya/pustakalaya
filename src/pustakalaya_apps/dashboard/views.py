from django.shortcuts import render
from django.views.generic.edit import UpdateView
from pustakalaya_apps.pustakalaya_account.models import UserProfile
from django.contrib.auth.decorators import login_required
from pustakalaya_apps.document.models import Document
from pustakalaya_apps.favourite_collection.models import Favourite
from django.core.exceptions import ObjectDoesNotExist



@login_required()
def dashboard(request):
    popular_documents = Document.objects.order_by('-updated_date')[:5]

    # Now lets get the users books first
    item_list = Favourite.objects.filter(favourite_item_type="document", user=request.user)

    document_fav_list = []

    for item in item_list:
        var = Document.objects.get(pk=item.favourite_item_id)
        document_fav_list.append(var)

    return render(request, "dashboard/dashboard_base.html", {
        'popular_documents': popular_documents,
        'favourite_documents':document_fav_list
    })


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








