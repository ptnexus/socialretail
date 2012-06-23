# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import Utilizador
import json


def list_promotions(request,*kwargs):
	return render(request, 'facebook/promotions_user.html', {},)
	
def list_history_promotions(request,*kwargs):
	return render(request, 'facebook/promotions_user_history.html', {},)
	
def list_friendsgroup(request,*kwargs):
	return render(request, 'facebook/friendsgroups.html', {},)