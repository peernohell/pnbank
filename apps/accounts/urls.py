# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'pnbank.apps.accounts.views',

    # new
    #url(r'^new/$', 'create_account', name='account_add'),

    # view account
    url(r'^view/(?P<account_id>\d+)/$', 'view_account', name='account_view'),

    # edit account
    #url(r'^edit/(?P<account_id>\d+)/$', 'update_account', name='account_edit'),

    # list accounts
    url(r'^all/$', 'list_accounts', name='account_list'),

    # delete account
    #url(r'^delete/(?P<account_id>\d+)/$', 'delete_account', name='account_delete'),
)
