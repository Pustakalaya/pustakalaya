from django.conf.urls import url
from . import views

# Application level namespace.
app_name = "show_featured"

urlpatterns = [
    # /show_featured/
    url(r'^$', views.show_all_featured_item, name="show_all_featured_item"),

]
