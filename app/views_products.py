# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Utilizador
from login import Login,access_required
import json

@access_required
def list(request,*kwargs):
	return render(request, 'facebook/products.html', {},)