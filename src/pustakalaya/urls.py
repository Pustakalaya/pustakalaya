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
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from . import views

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Url patterns that don't need to localize
urlpatterns = [
    # Change language
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # Hit count
    url(r'^hitcount/', include('hitcount.urls', namespace='hitcount')),

    # /review_input
    url(r'^review_system/', include('pustakalaya_apps.review_system.urls', namespace="review_system")),

    # /review_delete
    url(r'^review_system/delete/', include('pustakalaya_apps.review_system.urls', namespace="review_system_delete")),

    # /review_edi
    url(r'^review_edit/edit/', include('pustakalaya_apps.review_system.urls', namespace="review_system_edit")),

    # /review_input
    url(r'^favourite_collection/', include('pustakalaya_apps.favourite_collection.urls', namespace="favourite_collection")),

    # /review_input
    url(r'^favourite_collection/favourite_remove/',include('pustakalaya_apps.favourite_collection.urls', namespace="favourite_collection_remove")),

    # Document App
    # /documents/
    url(r'^documents/', include('pustakalaya_apps.document.urls', namespace="document")),

    # Video app
    # /videos/
    url(r'^videos/', include('pustakalaya_apps.video.urls', namespace="video")),

    # Audio app
    # /audios/
    url(r'^audios/', include('pustakalaya_apps.audio.urls', namespace="audio")),

]

# Enable i18n based urls
urlpatterns += i18n_patterns(
    # Search endpoint
    url(r'^search/', include('pustakalaya_apps.pustakalaya_search.urls', namespace="search")),

    # Browse endpoint url
    url(r'^browse/', include('pustakalaya_apps.pustakalaya_search.browse_urls', namespace="browse")),

    # Homepage and core urls
    url(r'^', include('pustakalaya_apps.core.urls', namespace="core")),

    # Community page aka category
    # /community/literatures-and-arts/
    # url(r'^category/', include('pustakalaya_apps.collection.urls', namespace="community")),
    url(r'^collection/', include('pustakalaya_apps.collection.urls', namespace="collection")),
    url(r'^community/', include('pustakalaya_apps.collection.community_urls', namespace="community")),

    # Author url
    # /authors/
    # Don't change this hard links are used.
    url(r'^authors/', include('pustakalaya_apps.core.author_urls', namespace="author")),

    # /keywords
    url(r'^keywords/', include('pustakalaya_apps.core.keyword_urls', namespace="keyword")),

    # Ratings.
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),


    # Wikipedia app
    # TODO:

    # Maps app
    # TODO:

    # Dashboard app
    # /dashboard/
    url(r'^dashboard/', include('pustakalaya_apps.dashboard.urls', namespace="dashboard")),

    # Django Admin jet
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),

    # Authentication urls
    url(r'^accounts/', include('allauth.urls')),

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
        r'^signup/$', TemplateView.as_view(template_name="static_pages/sign_up.html"),
        name="signup"
    ),
    # Help page
    # /help/
    url(
        r'^help/$', TemplateView.as_view(template_name="static_pages/help.html"),
        name="help"
    ),
    # Forget password
    # /forget-password/
    url(
        r'^forget-password/$', TemplateView.as_view(template_name="static_pages/forgetpassword.html"),
        name="forget-password"
    ),
    prefix_default_language=True   ,
)

if settings.DEBUG:
    # Serve media in development mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
