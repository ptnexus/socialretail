# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import CustomUser,WishList
from login import Login,access_required
import json
from django.core.paginator import Paginator
from forms import WishListForm


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


from django.forms.models import inlineformset_factory
@access_required
def edit_or_create(request,pk,*kwargs):
	user = Login(request).getUser()
	if pk is None:
		wishlist = WishList(user = user)
	else:
		wishlist = user.wishlist_set.get(pk=pk)
		
	if request.POST:
		form = WishListForm(request.POST,instance = wishlist)
		if form.is_valid():
			if form.save():
				return redirect('wishlists-list')
	else:
		form = WishListForm(instance = wishlist)
	return render(request, 'facebook/wishlist_' + ( 'create.html'  if pk is None else 'edit.html'), {
		'form': form,
	},)

@access_required
def remove(request,pk,*kwargs):
	try:
		Login(request).getUser().wishlist_set.get(pk=pk).delete()
	except:
		pass
	return redirect('wishlists-list')