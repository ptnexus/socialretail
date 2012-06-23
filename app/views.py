# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import Utilizador
import json



def test(request,*kwargs):
	
	
	return render(request, 'facebook/index.html', {"users": Utilizador.objects.all()},)
	#return HttpResponse(json.dumps(map(lambda x:{'name':x.nome,'email':x.email},Utilizador.objects.all())), mimetype="application/json")
	
def login(request,*kwargs):
	return render(request, 'login.html', {},)