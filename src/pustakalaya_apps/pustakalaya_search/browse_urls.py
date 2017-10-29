"""
urls to browse all items.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Search url
    url(r'^$', views.browse, name="browse_all"),
    url(r'^(?P<browse_by>[\w]+)/$', views.browse, name="browse"),


]
