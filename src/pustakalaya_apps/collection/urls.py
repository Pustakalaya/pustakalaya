from django.conf.urls import url
from . import views

# Application level namespace.
app_name = "collection"

urlpatterns = [

    url(
        r'(?P<name>\w+)/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',
        views.collection_detail, name="collection_detail"
    ),

]
