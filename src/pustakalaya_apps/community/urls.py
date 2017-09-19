from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views



urlpatterns = [
    url(r'teardown/$', views.teardown),
    url(r'^$', cache_page(60 * 15)(views.index)),

]