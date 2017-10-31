"""
urls to browse all items.
"""
from django.conf.urls import url
from . import browse_views

urlpatterns = [
    # Search url
    url(r'^$', browse_views.browse, name="browse"),
    #url(r'^(?P<browse_by>[\w]+)/$', browse_views.browse, name="browse"),


]
