from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/?$', 'retailer.views.home', name='retailer-home-view'),
    url(r'^about_us$', 'retailer.views.about_us', name='retailer-about-us-view'),
    url(r'^login/?$', 'retailer.views.login', name='retailer-login-view'),
    url(r'^logout/?$', 'retailer.views.logout', name='retailer-logout-view'),
)

urlpatterns += patterns('',
    url(r'^products/?$', 'retailer.views_products.list', name='retailer-products-list'),
    url(r'^product/(?P<pk>\d+)/?$', 'retailer.views_products.detail', name='retailer-product-detail'),
)

urlpatterns += patterns('',
    url(r'^promotions_user/?$', 'retailer.views_profile.list_promotions', name='retailer-promotion-list'),
    url(r'^promotions_user_history/?$', 'retailer.views_profile.list_history_promotions', name='retailer-promotion-history-list'),
)