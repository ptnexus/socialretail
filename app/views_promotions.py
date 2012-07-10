# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import CustomUser,Promotion
from django.db.models import Q
from login import Login,access_required,access_required_ajax
from myjson import MyJson

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

@access_required
def promotion_detail(request,pk,*kwargs):
	promotion = None
	try:
		
		promotion = Promotion.objects.get(pk=pk)
		
				
	except:
		request.flash['error'] = 'Error in request'
		return redirect('profile-promotion-list')
	
	return render(request, 'facebook/promotion/detail.html', {
		'promotion': promotion,
		'product': promotion.product,
		'retailer': promotion.retailer,
	},)
	
@access_required_ajax
def promotion_detail_ajax(request,pk,*kwargs):
	json = MyJson(request)
	try:
		promotion = Promotion.objects.get(pk=pk)
		user = Login(request).getUser()
		inPromotion = promotion.userInPromotion(user)
		friendsInPromotion = []
		if inPromotion:
			friendsInPromotion = user.promotion_group_users.get(promotion=promotion).users.exclude(user=user).all()
		
		data = render(request, 'facebook/promotion/tab_detail.html', {
					'promotion': promotion,
					'product': promotion.product,
					'retailer': promotion.retailer,
					'inPromotion':inPromotion,
					'friendsInPromotion':friendsInPromotion,
					'friendsNeed':promotion.elements_number-1-len(friendsInPromotion)
				},
				).content
		json.setOk()
		json.addData(data)
	except Exception,e:
		json.setError()
		json.addError(str(e))
	
	return json.getJsonRequest()



@access_required_ajax
def promotion_detail_groups_ajax(request,pk,*kwargs):
	json = MyJson(request)
	try:
		
		promotion = Promotion.objects.get(pk=pk)
		user = Login(request).getUser()
		inPromotion = promotion.userInPromotion(user)
		friendsInPromotion = []
		if inPromotion:
			friendsInPromotion = user.promotion_group_users.get(promotion=promotion).users.exclude(user=user).all()
		
		data = render(request, 'facebook/promotion/tab_groups.html', {
					'promotion': promotion,
					'product': promotion.product,
					'retailer': promotion.retailer,
					'inPromotion':inPromotion,
					'friendsInPromotion':friendsInPromotion,
					'friendsNeed':promotion.elements_number-1-len(friendsInPromotion)
				},
				).content
		json.setOk()
		json.addData(data)
	except Exception,e:
		json.setError()
		json.addError(str(e))
	
	return json.getJsonRequest()



@access_required_ajax
def promotion_detail_groups_table_ajax(request,pk,*kwargs):
	json = MyJson(request)
	promotion = Promotion.objects.get(pk=pk)
	user = Login(request).getUser()
	field_order = ''
	
	users = user.friends.all()
	
	promotions = promotion.promotionGroups.filter(users__in = users)
	""""	
	if request.POST.get('qtype',None) is not None:
		if request.POST.get('qtype',None) == 'name':
			users = users.filter( name__icontains= request.POST.get('query','') )
		elif request.POST.get('qtype',None) == 'groups':
			users = users.filter( 
				custom_user_friends_groups__user = user,
				custom_user_friends_groups__name__icontains = request.POST.get('query','') 
			)
	
	if request.POST.get('sortorder','') != 'asc':
		field_order = '-'
	if 'sortname' in request.POST:
		if request.POST.get('sortname','') == 'name' :
			users = users.order_by(field_order+'name')
		
	else:
		users = users.order_by(field_order+'name')	
    """
	promotions = promotions.distinct()
	paginator = Paginator(promotions.all(), request.POST.get('rp',15))
	try:
		page = int(request.POST.get('page',1))
	except:
		page = 1
		
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
	rows = paginator.page(page)
	data = {
		'page': page,
		'total':promotions.count(),
		'rows':[],
	}
	
	for o in rows:
		data['rows'].append({
			'id': o.pk,
			'cell':{
				'createDate':str(o.create_date),
				'creator':o.user.name,
				'yourFriends':o.getFriendsByUser(user,users) ,
				'friendsLeft': o.promotion.elements_number-o.users.count(),
			},
			
		})
	return json.transformeJsonRequest(data)


@access_required_ajax
def promotion_detail_friends_ajax(request,pk,*kwargs):
	json = MyJson(request)
	try:
		
		promotion = Promotion.objects.get(pk=pk)
		user = Login(request).getUser()
		inPromotion = promotion.userInPromotion(user)
		friendsInPromotion = []
		if inPromotion:
			friendsInPromotion = user.promotion_group_users.get(promotion=promotion).users.exclude(user=user).all()
		
		data = render(request, 'facebook/promotion/tab_friends.html', {
					'promotion': promotion,
					'product': promotion.product,
					'retailer': promotion.retailer,
					'inPromotion':inPromotion,
					'friendsInPromotion':friendsInPromotion,
					'friendsNeed':promotion.elements_number-1-len(friendsInPromotion)
				},
				).content
		json.setOk()
		json.addData(data)
	except Exception,e:
		json.setError()
		json.addError(str(e))
	
	return json.getJsonRequest()
	

@access_required_ajax
def promotion_detail_friends_table_ajax(request,pk,*kwargs):
	json = MyJson(request)
	promotion = Promotion.objects.get(pk=pk)
	user = Login(request).getUser()
	field_order = ''
	
	users = user.friends.exclude(pk=user.pk)
	
	if request.POST.get('qtype',None) is not None:
		if request.POST.get('qtype',None) == 'name':
			users = users.filter( name__icontains= request.POST.get('query','') )
		elif request.POST.get('qtype',None) == 'groups':
			users = users.filter( 
				custom_user_friends_groups__user = user,
				custom_user_friends_groups__name__icontains = request.POST.get('query','') 
			)
	if request.POST.get('sortorder','') != 'asc':
		field_order = '-'
	if 'sortname' in request.POST:
		if request.POST.get('sortname','') == 'name' :
			users = users.order_by(field_order+'name')
		
	else:
		users = users.order_by(field_order+'name')	
	print dir(user)
	users = users.all()
	paginator = Paginator(users.all(), request.POST.get('rp',15))
	try:
		page = int(request.POST.get('page',1))
	except:
		page = 1
		
	if page > paginator.num_pages:
		page = paginator.num_pages
	if page < 1:
		page = 1
	rows = paginator.page(page)
	data = {
		'page': page,
		'total':users.count(),
		'rows':[],
	}
	
	for o in rows:
		data['rows'].append({
			'id': o.pk,
			'cell':{
				'photo':o.getTablePhoto(),
				'name':o.name,
				'groups':o.getGroupsNamesByUser(user) ,
				'idInvited': 'Yes' if o.isInvited(user,promotion) else 'No',
			},
			
		})
	return json.transformeJsonRequest(data)
	
	


	
	
	
	
