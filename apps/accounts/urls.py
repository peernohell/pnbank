# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'pnbank.apps.accounts.views',

    # new account
    url(r'^new/$', 'create_account', name='create_account'),
    # view account
    url(r'^view/(?P<account_id>\d+)/$', 'view_account', name='view_account'),
    # edit account
    url(r'^edit/(?P<account_id>\d+)/$', 'update_account', name='update_account'),
    # list accounts
    url(r'^all/$', 'list_accounts', name='list_accounts'),
    # delete account
    url(r'^delete/(?P<account_id>\d+)/$', 'delete_account', name='delete_account'),

    # new entry
    url(r'^new_entry/$', 'create_entry', name='create_entry'),
    url(r'^(?P<account_id>\d+)/new_entry/$', 'create_entry', name='create_entry'),
    # view entry
    url(r'^view_entry/(?P<entry_id>\d+)/$', 'view_entry', name='view_entry'),
    url(r'^(?P<account_id>\d+)/view_entry/(?P<entry_id>\d+)/$', 'view_entry', name='view_entry'),
    # edit entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', 'update_entry', name='update_entry'),
    url(r'^(?P<account_id>\d+)/edit_entry/(?P<entry_id>\d+)/$', 'update_entry', name='update_entry'),
    # list entries
    url(r'^all_entries/$', 'list_entries', name='list_entries'),
    url(r'^(?P<account_id>\d+)/all_entries/$', 'list_entries', name='list_entries'),
    # delete entry
    url(r'^delete_entry/(?P<entry_id>\d+)/$', 'delete_entry', name='delete_entry'),
    url(r'^(?P<account_id>\d+)/delete_entry/(?P<entry_id>\d+)/$', 'delete_entry', name='delete_entry'),

)
