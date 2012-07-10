from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponsePermanentRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialretail.views.home', name='home'),
    url(r'^/?$', lambda request: HttpResponsePermanentRedirect('application')),
    url(r'^application/', include('app.urls')),
	
	
	url(r'^backoffice/', include('retailer.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
