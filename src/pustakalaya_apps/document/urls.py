from django.conf.urls import url
from . import views

# Application level namespace.
app_name = "document"

urlpatterns = [
    # /documents/
    url(r'^$', views.documents, name="documents"),

    # /documents/<document_id>
    url(r'^(?P<pk>\w+)', views.document_detail, name="document_detail")
]
