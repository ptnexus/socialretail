from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.test', name='home-view'),
    url(r'login/?$', 'app.views.login', name='login-view'),
    url(r'retailers/?$', 'app.views_retailers.list', name='retailers-list'),
	url(r'wishlists/?$', 'app.views_wishlists.list', name='wishlists-list'),
	url(r'products/?$', 'app.views_products.list', name='products-list'),
	url(r'promotions/?$', 'app.views_promotions.list', name='promotions-list'),
	
	url(r'promotions_user/?$', 'app.views_profile.list_promotions', name='profile-promotion-list'),
	url(r'promotions_user_history/?$', 'app.views_profile.list_history_promotions', 
			name='profile-promotion-history-list'),
	url(r'friends/?$', 'app.views_profile.list_friendsgroup',name='profile-friendsgroup-list'),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)


