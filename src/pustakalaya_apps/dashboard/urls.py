from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^profile/$', views.profile, name="profile"),
    # /dashboard/profile/edit/
    url(r'^profile/edit/(?P<pk>\d+)/$', views.ProfileEdit.as_view(), name="profile_edit")
]
