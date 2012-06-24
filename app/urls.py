from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home-view'),
    url(r'login/?$', 'app.views.login', name='login-view'),
    url(r'logout/?$', 'app.views.logout', name='logout-view'),
    url(r'retailers/?$', 'app.views_retailers.list', name='retailers-list'),
	url(r'wishlists/?$', 'app.views_wishlists.list', name='wishlists-list'),
	url(r'products/?$', 'app.views_products.list', name='products-list'),
	url(r'promotions/?$', 'app.views_promotions.list', name='promotions-list'),
	
	url(r'promotions_user/?$', 'app.views_profile.list_promotions', name='profile-promotion-list'),
	url(r'promotions_user_history/?$', 'app.views_profile.list_history_promotions', 
			name='profile-promotion-history-list'),
	url(r'friendsgroups/?$', 'app.views_profile.list_friendsgroup',name='profile-friendsgroup-list'),
	url(r'friendsgroups_create/?$', 'app.views_profile.create_friendsgroup',name='profile-friendsgroup-create'),
	
	url(r'friendsgroups_edit/(?P<pk>\d)/?$', 'app.views_profile.edit_friendsgroup',name='profile-friendsgroup-edit'),
	url(r'loaddata/?$', 'app.views.loaddata',name='loaddata-view'),
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
)


