from django.shortcuts import render
from django.views.decorators.cache import cache_page, never_cache


from .models import Community


@never_cache
def teardown(request):
    c = Community.objects.all()
    c = Community.objects.all()[0]
    return  render(request, 'community/detail.html', {'c':c})



@cache_page(60 * 2)
def index(request):
    # Grab all the communities from a table
    c = Community.objects.all()
    return render(request, 'community/index.html', {'c':c})



