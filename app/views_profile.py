# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from models import Utilizador,UtilizadoresGrupos
from login import Login,access_required
from forms import UtilizadoresGruposForm
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.forms.util import ErrorList

import json

@access_required
def list_promotions(request,*kwargs):
	return render(request, 'facebook/promotions_user.html', {},)
	
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
		groups = user.utilizadoresgrupos_set.filter(nome__contains = search)
	else:
		groups = user.utilizadoresgrupos_set.all()
	
	return render(request, 'facebook/friendsgroups.html', {
		'groups': groups,
		'search':search,
	},)
	
@access_required
def create_friendsgroup(request,*kwargs):
	user = Login(request).getUser()
	if request.POST:
		form = UtilizadoresGruposForm(request.POST)
		if form.is_valid():
			#form['utilizador_id'] = Login(request).getUser().pk
			ug = form.save(commit=False)
			ug.utilizador = Login(request).getUser()
			try:
				ug.full_clean()
				ug.save()
				return redirect('profile-friendsgroup-list')
			except ValidationError as e:
				
				print dir(e)
				for k in list(e.message_dict):
					errors = form._errors.setdefault(k, ErrorList())
					errors.append( e.message_dict[k] )
					#form._errors[k] = 
			
	else:
		form = UtilizadoresGruposForm()
	return render(request, 'facebook/friendsgroups_create.html', {
		'form': form,
	},)
@access_required
def edit_friendsgroup(request,pk,*kwargs):
	user = Login(request).getUser()
	group = user.utilizadoresgrupos_set.get(pk=pk)
	if request.POST:
		form = UtilizadoresGruposForm(request.POST)
		if form.is_valid():
			#form['utilizador_id'] = Login(request).getUser().pk
			ug = form.save(commit=False)
			ug.utilizador = Login(request).getUser()
			try:
				ug.full_clean()
				ug.save()
				return redirect('profile-friendsgroup-list')
			except ValidationError as e:
				
				print dir(e)
				for k in list(e.message_dict):
					errors = form._errors.setdefault(k, ErrorList())
					errors.append( e.message_dict[k] )
					#form._errors[k] = 
			
	else:
		form = UtilizadoresGruposForm(instance = group)
	return render(request, 'facebook/friendsgroups_edit.html', {
		'form': form,
	},)