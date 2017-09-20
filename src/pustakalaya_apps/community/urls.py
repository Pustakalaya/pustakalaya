from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views



urlpatterns = [
    url(r'cache_request/$', views.cache_request),
    url(r'community_detail/$', views.community_detail),
    #url(r'teardown/$', views.teardown),
    url(r'^$', views.index), # Cache for 15 minutes.

]