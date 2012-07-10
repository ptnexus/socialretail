from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'retailer.views.home', name='retailer-home-view'),
    url(r'^login/?$', 'retailer.views.login', name='retailer-login-view'),
    url(r'^logout/?$', 'retailer.views.logout', name='retailer-logout-view'),
)
