# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'pnbank.apps.accounts.views',

    # new
    url(r'^new/$', 'create_account', name='create_account'),

    # view account
    url(r'^view/(?P<account_id>\d+)/$', 'view_account', name='view_account'),

    # edit account
    url(r'^edit/(?P<account_id>\d+)/$', 'update_account', name='update_account'),

    # list accounts
    url(r'^all/$', 'list_accounts', name='list_accounts'),

    # delete account
    url(r'^delete/(?P<account_id>\d+)/$', 'delete_account', name='delete_account'),
)
