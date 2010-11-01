# -*- coding: utf-8 -*-
""" fichier de description des URLs accessibles """
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pnbank.apps.core.views',
                       url(r'^$', 'index', name = 'index'),
)
