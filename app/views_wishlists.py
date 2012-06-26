# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import CustomUser,WishList,WishListProduct
from login import Login,access_required
import json
from django.core.paginator import Paginator
from forms import WishListProductForm


@access_required
def list(request,*kwargs):
	user = Login(request).getUser()
	wishlists = []
	search = ''
	if 'search' in request.POST and request.POST['search'] != '':
		search = request.POST['search']
		wishlists = WishList.objects.filter(user = user, name__contains = search)
	else:
		wishlists = WishList.objects.filter(user = user)
	paginator = Paginator(wishlists, 10)
	try:
		page = int(request.GET.get('page',1))
	except:
		page = 1
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
	return render(request, 'facebook/wishlists.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)