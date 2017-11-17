from django.conf.urls import url
from . import views
from . import collection_views

urlpatterns = [

    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^profile/$', views.profile, name="profile"),
    # /dashboard/profile/edit/
    url(r'^profile/edit/(?P<pk>\d+)/$', views.ProfileEdit.as_view(), name="profile_edit"),
    # dashboard/add/document/
    url(r'^document/add/$', views.AddDocument.as_view(), name="document_add"),
    url(r'^collection/add/$', collection_views.AddCollection.as_view(), name="document_add"),
    #/dashboard/collections/
    url(r'^collection/add/$', collection_views.AddCollection.as_view(), name="collection_list"),
]
