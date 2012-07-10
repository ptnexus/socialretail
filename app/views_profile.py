# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from models import CustomUser,CustomUserGroup,Promotion,PromotionGroup
from login import Login,access_required
from forms import CustomUserGroupForm
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.forms.util import ErrorList
from django.core.paginator import Paginator

import json

@access_required
def list_promotions(request,*kwargs):
	
	user = Login(request).getUser()
	promotions = []
	search = ''
	if 'search' in request.POST and request.POST['search'] != '':
		search = request.POST['search']
		promotions = PromotionGroup.objects.filter(promotion__name_icontains = search).select_related('promotion')
	else:
		promotions = PromotionGroup.objects.select_related('promotion')
	paginator = Paginator(promotions, 10)
	try:
		page = int(request.GET.get('page',1))
	except:
		page = 1
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
		
	return render(request, 'facebook/promotions_user.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)
	
@access_required
def list_history_promotions(request,*kwargs):
	return render(request, 'facebook/promotions_user_history.html', {},)

@access_required
def list_friendsgroup(request,*kwargs):
	
	user = Login(request).getUser()
	groups = []
	search = ''
	if 'search' in request.POST and request.POST['search'] != '':
		search = request.POST['search']
		groups = user.customusergroup_set.filter(name__icontains = search)
	else:
		groups = user.customusergroup_set.all()
	paginator = Paginator(groups, 10)
	try:
		page = int(request.GET.get('page',1))
	except:
		page = 1
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
		
	return render(request, 'facebook/friendsgroups.html', {
		'paginator': paginator,
		'search':search,
		'page': paginator.page(page),	
		'page_number':page,
	},)
	
@access_required
def edit_or_create_friendsgroup(request,pk,*kwargs):
	user = Login(request).getUser()
	if pk is None:
		group = CustomUserGroup(user = Login(request).getUser())
	else:
		group = user.customusergroup_set.get(pk=pk)
		
	if request.POST:
		form = CustomUserGroupForm(request.POST,instance = group)
		if form.is_valid():
			if form.save():
				request.flash['message'] = 'Edit friendsgroup with success' if pk is not None else 'Add friendsgroup with success'
				return redirect('profile-friendsgroup-list')
		else:
			request.flash['error'] = 'Please review all errors above'
	else:
		form = CustomUserGroupForm(instance = group)
	return render(request, 'facebook/friendsgroups_' + ( 'create.html'  if pk is None else 'edit.html'), {
		'form': form,
		'group':group,
	},)
	
@access_required
def remove_friendsgroup(request,pk,*kwargs):
	try:
		Login(request).getUser().customusergroup_set.get(pk=pk).delete()
		request.flash['message'] = 'Removed friendsgroup with success'
	except:
		pass
	return redirect('profile-friendsgroup-list')
	
	
