# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from models import CustomUser,CustomUserGroup,Promotion,PromotionGroup,Product, WishList,Retailer
from login import Login,access_required_ajax
from forms import CustomUserGroupForm,WishListProductForm
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.forms.util import ErrorList
from django.core.paginator import Paginator

from myjson import MyJson
import json
from django.template.loader import render_to_string

@access_required_ajax
def wishlist(request,product_pk,*kwargs):
	json = MyJson(request)
	try:
		product = Product.objects.get(pk= int(product_pk) )
	except Exception,e:
		json.setError()
		json.addError('Product don\'t exit.')
		
	if not json.isError():
		user = Login(request).getUser()
		wish = WishList(user = user)
		try:
			wishlistform = WishListProductForm(instance = wish )
			if request.POST:
				if 'action' in request.POST and request.POST.get('action','') == 'create_wishlist':
					wishlistform = WishListProductForm(request.POST,instance = wish )
					if wishlistform.is_valid():
						wish = wishlistform.save()
						wish.products = [product]
				if 'pk' in request.POST and request.POST.get('pk',None) is not None:
					try:
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_remove':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).delete()
							
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_remove_product':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).products.remove(product)
	
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_add_product':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).products.add(product)

					except Exception,e:
							pass
			wishlist = user.wishlist_set.all()
			for w in wishlist:
				w.hasProduct = w.products.filter(pk=product.pk).exists()
			
			data = render(request,'facebook/ajax/wishlists.html',{
				'wishlists':wishlist,
				'wishlistform':wishlistform,
				'product':product,
			} ).content
			json.setOk()
			json.addData(data)
		except Exception,e:
			json.setError()
			json.addError(str(e))
	return json.getJsonRequest()


@access_required_ajax
def promotions(request,product_pk,*kwargs):
	json = MyJson(request)
	try:
		product = Product.objects.get(pk= int(product_pk) )
	except Exception,e:
		json.setError()
		json.addError('Product don\'t exit.')
		
	if not json.isError():
		user = Login(request).getUser()
		promotions =  product.promotion_set.all()
		try:
			"""
			wishlistform = WishListProductForm(instance = wish )
	
			if request.POST:
				if 'action' in request.POST and request.POST.get('action','') == 'create_wishlist':
					wishlistform = WishListProductForm(request.POST,instance = wish )
					if wishlistform.is_valid():
						wish = wishlistform.save()
						wish.products = [product]
				if 'pk' in request.POST and request.POST.get('pk',None) is not None:
					try:
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_remove':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).delete()
							
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_remove_product':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).products.remove(product)
	
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_add_product':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).products.add(product)

					except Exception,e:
							pass
					
			wishlist = user.wishlist_set.all()
			for w in wishlist:
				w.hasProduct = w.products.filter(pk=product.pk).exists()
			"""
			
			data = render(request,'facebook/ajax/promotions.html',{
				'promotions':map(lambda x: x.getPromotionInfo(user), promotions),
				#'wishlistform':wishlistform,
				'product':product,
				'flash':request.flash,
			} ).content
			#return HttpResponse(data)
			json.setOk()
			json.addData(data)
		except Exception,e:
			json.setError()
			json.addError(str(e))
	return json.getJsonRequest()

@access_required_ajax
def retailer_promotions(request,retailer_pk,*kwargs):
	json = MyJson(request)
	try:
		retailer = Retailer.objects.get(pk= int(retailer_pk) )
	except Exception,e:
		json.setError()
		json.addError('Product don\'t exit.')
		
	if not json.isError():
		user = Login(request).getUser()
		promotions =  retailer.promotion_set.all()
		try:
			"""
			wishlistform = WishListProductForm(instance = wish )
	
			if request.POST:
				if 'action' in request.POST and request.POST.get('action','') == 'create_wishlist':
					wishlistform = WishListProductForm(request.POST,instance = wish )
					if wishlistform.is_valid():
						wish = wishlistform.save()
						wish.products = [product]
				if 'pk' in request.POST and request.POST.get('pk',None) is not None:
					try:
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_remove':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).delete()
							
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_remove_product':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).products.remove(product)
	
						if 'action' in request.POST and request.POST.get('action','') == 'wishlist_add_product':
								user.wishlist_set.get(pk= request.POST.get('pk',None) ).products.add(product)

					except Exception,e:
							pass
					
			wishlist = user.wishlist_set.all()
			for w in wishlist:
				w.hasProduct = w.products.filter(pk=product.pk).exists()
			"""
			data = render(request,'facebook/ajax/promotions.html',{
				'promotions':map(lambda x: x.getPromotionInfo(user), promotions),
				#'wishlistform':wishlistform,
				'retailer':retailer,
			} ).content
			json.setOk()
			json.addData(data)
		except Exception,e:
			json.setError()
			json.addError(str(e))
	return json.getJsonRequest()
