from django.conf.urls import url
from . import keyword_views

urlpatterns = [

    # /keywords/<keyword>/<keyword_id>
    url(
        r'^(?P<keyword>[\w-]+)/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',
        keyword_views.KeywordDetail.as_view(),
        name="keyword_detail"

    ),

]
