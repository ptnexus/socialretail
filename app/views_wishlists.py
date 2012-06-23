# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from models import Utilizador
import json


def list(request,*kwargs):
	return render(request, 'facebook/wishlists.html', {},)