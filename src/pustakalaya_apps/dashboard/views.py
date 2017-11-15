from django.shortcuts import render
from django.shortcuts import render;


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
