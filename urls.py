from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pnbank/', include('pnbank.accounts.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
  (r'^accounts/login/$', 'django.contrib.auth.views.login'),
  (r'^accounts/$', 'pnbank.accounts.views.index'),
  (r'^accounts/(?P<account_id>\d+)$', 'pnbank.accounts.views.show'),
#    (r'^accounts/(?P<account_id>)\new$', 'pnbank.accounts.views.new'),
#    (r'^accounts/(?P<account_id>)\d+/edit$', 'pnbank.accounts.views.edit'),
    
    # Uncomment the next line to enable the admin:
  (r'^admin/', include(admin.site.urls)),
  (r'^$', 'pnbank.accounts.views.index')
)
