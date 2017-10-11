"""pustakalaya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from . import views

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [

    # Homepage and core urls
    url(r'^', include('pustakalaya_apps.core.urls', namespace="core")),

    # Document App
    # /documents/
    url(r'^documents/', include('pustakalaya_apps.document.urls', namespace="document")),

    # Video app
    # /videos/
    url(r'^videos/', include('pustakalaya_apps.video.urls', namespace="video")),

    # Audio app
    # /audios/
    url(r'^audios/', include('pustakalaya_apps.audio.urls', namespace="audio")),

    # Wikipedia app
    # TODO:

    # Maps app
    # TODO:

    # Dashboard app
    # /dashboard/
    url(r'^dashboard/', include('pustakalaya_apps.dashboard.urls')),

    # Django Admin jet
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),

    ########################### Static Page urls ####################################

    # About page
    # /about/
    url(
        r'^about/$',
        cache_page(CACHE_TTL)(TemplateView.as_view(template_name="static_pages/about.html")),
        name="about"
    ),

    # Feedback page
    # /feedback/
    url(
        r'^feedback/$',
        views.feedback,
        name="feedback"
    ),

    # Help page
    # /help/
    url(
        r'^help/$', TemplateView.as_view(template_name="static_pages/help.html"),
        name="help"
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
