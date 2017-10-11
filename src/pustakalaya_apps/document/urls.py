from django.conf.urls import url
from . import views

# Application level namespace.
app_name = "document"

urlpatterns = [
    # /documents/
    url(r'^$', views.documents, name="documents"),

    # /documents/<document_id>
    url(r'^detail/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', views.DocumentDetailView.as_view(), name="document_detail")
]
