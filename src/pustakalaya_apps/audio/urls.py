from django.conf.urls import url
from . import views

# Application level namespace.
app_name = "audio"

urlpatterns = [
    # /documents/
    url(r'^$', views.audios, name="audios"),

    # /documents/<document_id>
    url(r'^(?P<title>).*/detail/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', views.AudioDetailView.as_view(), name="detail"),

    url(r'^detail/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', views.AudioDetailView.as_view(), name="detail_without_slug")
]


