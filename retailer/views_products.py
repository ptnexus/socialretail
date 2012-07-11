# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from app.models import Retailer,Product
from login import RetailerLogin, retailer_access_required
import json
from django.core.paginator import Paginator
#from forms import WishListProductForm


@retailer_access_required
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
	return render(request, 'retailer/products.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)
	
@retailer_access_required
def detail(request,pk,*kwargs):	
	try:
		object = Product.objects.get(pk=pk)
	except Exception,e:
		return redirect('retailer-products-list')
	user = RetailerLogin(request).getUser()
	promotions =  object.promotion_set.all()
	
	return render(request, 'retailer/product_detail.html', {
		'object': object,
		'promotions':map(lambda x: x.getPromotionInfo(user), promotions),
	},)
	
	return redirect('retailer-product-detail',pk = pk )
