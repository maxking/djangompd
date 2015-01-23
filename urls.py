from django.conf import settings
from django.conf.urls import patterns, include, url
from djangompd import urls
from mobile import urls as mobile_urls

urlpatterns = patterns('',
    url(r'', include(mobile_urls.urlpatterns)),
    url(r'ajax/', include(urls.urlpatterns)),

    (r'^m/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
