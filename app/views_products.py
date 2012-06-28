# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import CustomUser,Product,WishList
from login import Login,access_required
import json
from django.core.paginator import Paginator
from forms import WishListProductForm


@access_required
def list(request,*kwargs):	
	products = []
	search = ''
	if 'search' in request.POST and request.POST['search'] != '':
		search = request.POST['search']
		products = Product.objects.filter(name__contains = search)
	else:
		products = Product.objects.all()
	paginator = Paginator(products, 10)
	try:
		page = int(request.GET.get('page',1))
	except:
		page = 1
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
	return render(request, 'facebook/products.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)
@access_required
def detail(request,pk,*kwargs):	
	try:
		object = Product.objects.get(pk=pk)
	except Exception,e:
		return redirect('products-list')
	user = Login(request).getUser()
	promotions =  object.promotion_set.all()
	wish = WishList(user = user)
	#wish.products = [object]
	wishlistform = WishListProductForm(instance = wish )
	
	if request.POST:
		if 'action' in request.POST and request.POST.get('action','') == 'create_wishlist':
			wishlistform = WishListProductForm(request.POST,instance = wish )
			if wishlistform.is_valid():
				wish = wishlistform.save()
				wish.products = [object]
	
	
	return render(request, 'facebook/product_detail.html', {
		'object': object,
		'promotions':map(lambda x: x.getPromotionInfo(user), promotions),
		'wishlists':user.wishlist_set.all(),
		'wishlistform':wishlistform,
	},)

	
	
	return redirect('product-detail',pk = pk )
