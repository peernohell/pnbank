# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple', )

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', name = 'login'),
    url(r'^accounts/logout/$', 'logout_then_login', name = 'logout'),
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('pnbank.apps.accounts.urls')),
    url(r'^import/', include('csvimporter.urls')),
    url(r'^', include('pnbank.apps.core.urls')),

    url(r'^public/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True},
        name='static'),
)
