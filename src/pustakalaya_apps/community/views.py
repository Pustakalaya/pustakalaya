from django.shortcuts import render

from .models import Community

def index(request):
    # Grab all the communities from a table
    c = Community.objects.all()
    return render(request, 'community/index.html', {'c':c})