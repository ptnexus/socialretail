from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home-view'),
    url(r'^about_us$', 'app.views.about_us', name='about-us-view'),
    url(r'login/?$', 'app.views.login', name='login-view'),
    url(r'logout/?$', 'app.views.logout', name='logout-view'),
 
    
	
	
	
	
	
	
	
	
	
	url(r'loaddata/?$', 'app.views.loaddata',name='loaddata-view'),    
)

urlpatterns += patterns('',
	url(r'wishlists/?$', 'app.views_wishlists.list', name='wishlists-list'),
	url(r'wishlist_edit/(?P<pk>\d+)/?$', 'app.views_wishlists.edit_or_create', name='wishlist-edit'),
	url(r'wishlist_create/?$', 'app.views_wishlists.edit_or_create',{'pk':None}, name='wishlist-create'),
	url(r'wishlist_remove/(?P<pk>\d+)/?$', 'app.views_wishlists.remove', name='wishlist-remove'),
)

urlpatterns += patterns('',
    url(r'retailers/?$', 'app.views_retailers.list', name='retailers-list'),
    url(r'retailer/(?P<pk>\d+)/?$', 'app.views_retailers.detail', name='retailer-detail'),
)

urlpatterns += patterns('',
	url(r'products/?$', 'app.views_products.list', name='products-list'),
	url(r'product/(?P<pk>\d+)/?$', 'app.views_products.detail', name='product-detail'),
)

urlpatterns += patterns('',
	url(r'friendsgroups/?$', 'app.views_profile.list_friendsgroup', name='profile-friendsgroup-list'),
	
	url(r'friendsgroups_create/?$', 'app.views_profile.edit_or_create_friendsgroup', {'pk':None} ,name='profile-friendsgroup-create'),
	
	url(r'friendsgroups_edit/(?P<pk>\d+)/?$', 'app.views_profile.edit_or_create_friendsgroup',name='profile-friendsgroup-edit'),
	
	url(r'friendsgroups_remove/(?P<pk>\d+)/?$', 'app.views_profile.remove_friendsgroup',name='profile-friendsgroup-remove'),
	
)


urlpatterns += patterns('',
    url(r'retailers/?$', 'app.views_retailers.list', name='retailers-list'),
    url(r'retailer/(?P<pk>\d+)/?$', 'app.views_retailers.detail', name='retailer-detail'),
)


urlpatterns += patterns('',
	url(r'promotions_user/?$', 'app.views_profile.list_promotions', name='profile-promotion-list'),
	url(r'promotions_user_history/?$', 'app.views_profile.list_history_promotions', 
			name='profile-promotion-history-list'),
)


urlpatterns += patterns('',
	url(r'promotions/?$', 'app.views_promotions.list', name='promotions-list'),
)
