"""
Keyword urls to browse list of items based on keyword
"""

from django.conf.urls import url
from . import keyword_views

urlpatterns = [

    url(r'(?P<keyword>.*?)/$', keyword_views.keyword_detail, name="keyword_detail"),

]
