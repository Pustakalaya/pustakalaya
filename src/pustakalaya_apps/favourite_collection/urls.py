from django.conf.urls import url
from . import views

# Application level namespace.
app_name = "favourite_collection"

urlpatterns = [
    # /review_system/
    url(r'^$', views.favourite_collection_view, name="favourite_collection"),
    url(r'^favourite_remove/$', views.remove, name="favourite_collection"),

]
