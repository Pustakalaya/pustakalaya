"""
urls to browse all items.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Search url
    url(r'^$', views.browse, name="browse"),

]
