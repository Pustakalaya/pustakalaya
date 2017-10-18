from django.conf.urls import url
from . import views

urlpatterns = [
    # Search url
    url(r'^$', views.search, name="search"),

]
