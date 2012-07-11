# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import Retailer,Promotion,PromotionGroup
from login import RetailerLogin, retailer_access_required
#from forms import CustomUserGroupForm
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.forms.util import ErrorList
from django.core.paginator import Paginator

import json

@retailer_access_required
def list_promotions(request,*kwargs):
	
	user = RetailerLogin(request).getUser()
	promotions = []
	search = ''
	promotions = Promotion.objects.filter(retailer = user)
	if 'search' in request.POST and request.POST['search'] != '':
		search = request.POST['search']
		promotions = promotions.filter(product__name = search)
	
	promotions = promotions.all()
	paginator = Paginator(promotions, 10)
	try:
		page = int(request.GET.get('page',1))
	except:
		page = 1
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
		
	return render(request, 'retailer/promotions_user.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)
	
@retailer_access_required
def list_history_promotions(request,*kwargs):
	return render(request, 'retailer/promotions_user_history.html', {},)