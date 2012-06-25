# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect
from models import CustomUser,CustomUserGroup
from forms import LoginForm
from login import Login,access_required
from datetime import datetime
import json
from django.forms.util import ErrorList




@access_required
def home(request,*kwargs):
	return render(request, 'facebook/index.html', {},)
	#return HttpResponse(json.dumps(map(lambda x:{'name':x.nome,'email':x.email},Utilizador.objects.all())), mimetype="application/json")
	
def loaddata(request,*kwargs):
	u,c = CustomUser.objects.get_or_create(username = 'bruno',password = '123456',
		email = 'ssbv96@gmail.com',name = 'Bruno Sousa',
		birth_date = datetime.now(), )
	u.save()
	ug,c = CustomUserGroup.objects.get_or_create(user = u ,name = 'G1')
	ug.save()
	return redirect('home-view')
	
def login(request,*kwargs):
	
	form = LoginForm(request.POST if request.POST else None)
	if form.is_valid():
		login = Login(request)
		if( login.makeLogin(form) ):
			return redirect('home-view')
		else:
			errors = form._errors.setdefault("systemerror", ErrorList())
			errors.append(u'Dados de login Invalidos')
	return render(request, 'login.html', {
		'form': form, 
	},)

	
def logout(request,**kwargs):
	login = Login(request)
	login.logout()
	return redirect('login-view')