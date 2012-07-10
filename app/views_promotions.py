# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import CustomUser,Promotion
from django.db.models import Q
from login import Login,access_required

import json
from django.core.paginator import Paginator
	
@access_required
def list(request,*kwargs):	
	promotions = []
	search = ''
	if 'search' in request.POST and request.POST['search'] != '':
		search = request.POST['search']
		promotions = Promotion.objects.filter( 
			Q(product__name__icontains = search) | Q(retailer__name__icontains = search)
		)
	else:
		promotions = Promotion.objects.all()
	paginator = Paginator(promotions, 10)
	try:
		page = int(request.GET.get('page',1))
	except:
		page = 1
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
	return render(request, 'facebook/promotions.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)
