from django.shortcuts import render
from django.views.decorators.cache import cache_page


from .models import Community



# def teardown(request):
#     c = Community.objects.all()
#     c = Community.objects.all()[0]
#     return  render(request, 'community/detail.html', {'c':c})
# #


@cache_page(60 * 2)
def cache_request(request):
    # Grab all the communities from a table
    c = Community.objects.all()
    return render(request, 'community/index.html', {'c':c})








def index(request):
    # Grab all the communities from a table
    c = Community.objects.all()
    return render(request, 'community/index.html', {'c':c})


def community_detail(request):
    communities1 = Community.objects.raw('SELECT * FROM community')
    #print(communities1)
    communities = Community.objects.all()
    return render(request, 'community/detail.html', {'communities':communities})
