# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import CustomUser,Retailer
import json
from django.db.models import Q
from login import Login,access_required
from django.core.paginator import Paginator
	
@access_required
def list(request,*kwargs):	
	retailers = []
	search = ''
	if 'search' in request.POST and request.POST['search'] != '':
		search = request.POST['search']
		retailers = Retailer.objects.filter( 
			Q(name__icontains = search)
		)
	else:
		retailers = Retailer.objects.all()
	paginator = Paginator(retailers, 10)
	try:
		page = int(request.GET.get('page',1))
	except:
		page = 1
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
	return render(request, 'facebook/retailers.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)

