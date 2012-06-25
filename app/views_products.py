# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import CustomUser,Product
from login import Login,access_required
import json
from django.core.paginator import Paginator
	
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
	print dir(user)
	promotions =  object.promotion_set.all()
	print dir(user.wishlist_set.all()[0])
	return render(request, 'facebook/product_detail.html', {
		'object': object,
		'promotions':map(lambda x: x.getPromotionInfo(user), promotions),
		'wishlists':user.wishlist_set.all(),
	},)
