from django.conf.urls import url
from . import author_views

urlpatterns = [

    # /authors/<author_name>/<author_id>
    url(
        r'^(?P<author_name>[\w-]+)/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',
        author_views.AuthorDetail.as_view(),
        name="author_detail"

    ),

]
