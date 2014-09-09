"""
Content-management URL scheme
"""
from django.conf.urls import patterns, url

from weblines.apps.cms import api

# HTTP method mapping
pages_api = api.PagesAPI.as_view({
    'get': 'retrieve',
})

urlpatterns = patterns(
    '',
    url(r'^pages/(?P<slug>[\w-]+)/$',
        pages_api,
        name='pages-api'),
)
