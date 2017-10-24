from django.conf.urls import url
from . import community_views

# Application level namespace.


urlpatterns = [
    url(
        r'(?P<community_name>[-\w]+)/$',
        community_views.community_detail, name="community_detail"
    ),
]
