from django.shortcuts import render
from django.shortcuts import render;


def dashboard(request):
    return render(request, "dashboard/dashboard_base.html")
