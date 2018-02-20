from django.conf.urls import url
from . import views

# Application level namespace.
app_name = "review_system"

urlpatterns = [
    # /review_system/
    url(r'^$', views.review_system_view, name="review_system"),
    url(r'^delete/$', views.delete, name="review_system"),
    url(r'^edit/$', views.edit, name="review_system"),

]
