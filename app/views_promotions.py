# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from models import CustomUser,Promotion, PromotionGroup
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
            Q(active=True),
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
	promotion_status = 'close'
	try:
		
		promotion = Promotion.objects.get(pk=pk,active=True)
		user = Login(request).getUser()
		promotion_status = promotion.getPromotionStatusForUser(user)
			
	except Exception,e:
		#request.flash['error'] = 'Error in request'
		request.flash['error'] = str(e)
		return redirect('profile-promotion-list')
	
	return render(request, 'facebook/promotion/detail.html', {
		'promotion': promotion,
		'product': promotion.product,
		'retailer': promotion.retailer,
		'promotion_status':promotion_status,
	},)
	
@access_required_ajax
def promotion_detail_ajax(request,pk,*kwargs):
	json = MyJson(request)
	try:
		promotion = Promotion.objects.get(pk=pk)
		user = Login(request).getUser()
		promotion_status = promotion.getPromotionStatusForUser(user)
		inPromotion = promotion.userInPromotion(user)
		friendsInPromotion = []
		if inPromotion:
			pp = user.promotion_group_users.get(promotion=promotion)
			friendsInPromotion = pp.users.exclude(user=user).all()
		
		data = render(request, 'facebook/promotion/tab_detail.html', {
					'promotion': promotion,
					'product': promotion.product,
					'retailer': promotion.retailer,
					'inPromotion':inPromotion,
					'friendsInPromotion':friendsInPromotion,
					'friendsNeed':promotion.elements_number-1-len(friendsInPromotion),
					'promotion_status':promotion_status,
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
	
	promotions = promotion.promotionGroups.filter(users__in = users).exclude(users__in = [user])
	
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
			pp = user.promotion_group_users.get(promotion=promotion)
			friendsInPromotion = pp.users.exclude(user=user).all()
		
		data = render(request, 'facebook/promotion/tab_friends.html', {
					'promotion': promotion,
					'product': promotion.product,
					'retailer': promotion.retailer,
					'inPromotion':inPromotion,
					'friendsInPromotion':friendsInPromotion,
					'friendsNeed':promotion.elements_number-1-len(friendsInPromotion),
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
	
    users = user.friends.filter(active=True).exclude(pk=user.pk)
	
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
    users = users.all()

    print dir(user)

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
	
	

@access_required_ajax
def promotion_detail_groups_join_ajax(request,pk,*kwargs):
	json = MyJson(request)
	try:
		promotion = Promotion.objects.get(pk=pk)
		if not promotion.promotionIsActive():
			raise Exception('Promotion is not active')
		
		user = Login(request).getUser()
		
		if 'group' not in request.POST:
			raise Exception('Group don\'t exists')
		#user.promotions = 
		group_id = int( request.POST.get('group',None) )
		print group_id
		groups = promotion.promotionGroups.filter(users__in = [user])
		for g in groups.all():
			if g.win_date is None and g.active:
				g.users.remove(user)
			else:
				raise Exception('You are in a group that wins the promotion or the promotion is not active')
		
		pg = PromotionGroup.objects.get(promotion = promotion, pk=group_id,active=True,win_date__exact = None)
		pg.users.add(user)
		pg.postSave()
		data = {}
		json.addData(data)
		json.addMessage('You join with successfull')
		json.setOk()
	except Exception,e:
		json.setError()
		json.addError(str(e))
		
	return json.getJsonRequest()
	

@access_required_ajax
def promotion_detail_groups_leave_ajax(request,pk,*kwargs):
	json = MyJson(request)
	try:
		promotion = Promotion.objects.get(pk=pk)
		if not promotion.promotionIsActive():
			raise Exception('Promotion is not active')
		
		user = Login(request).getUser()
		
		groups = promotion.promotionGroups.filter(users__in = [user])
		for g in groups.all():
			if g.win_date is None and g.active:
				g.users.remove(user)
			else:
				raise Exception('You are in a group that wins the promotion or the promotion is not active')
		data = {}
		json.addData(data)
		json.addMessage('You leave with successfull')
		json.setOk()
	except Exception,e:
		json.setError()
		json.addError(str(e))
		
	return json.getJsonRequest()

@access_required_ajax
def promotion_detail_groups_create_ajax(request,pk,*kwargs):
	json = MyJson(request)
	try:
		promotion = Promotion.objects.get(pk=pk)
		if not promotion.promotionIsActive():
			raise Exception('Promotion is not active')
		user = Login(request).getUser()
		groups = promotion.promotionGroups.filter(users__in = [user])
		for g in groups.all():
			if g.win_date is None and g.active:
				g.users.remove(user)
			else:
				raise Exception('You are in a group that wins the promotion or the promotion is not active')
		pg,c = PromotionGroup.objects.get_or_create(user = user, promotion = promotion)
		if c:
			pg.save()
		pg.users.add(user)
		pg.postSave()
		
		data = {}
		json.addData(data)
		json.addMessage('You create a group with successfull')
		json.setOk()
	except Exception,e:
		json.setError()
		json.addError(str(e))
		
	return json.getJsonRequest()
	
	
	
