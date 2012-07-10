# -*- coding: utf-8 -*-

from app.models import Retailer

from app.myjson import MyJson

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from functools import wraps


class RetailerLogin(object):
	def __init__(self,request,**kwargs):
		self.request = request
		super(RetailerLogin,self).__init__(**kwargs)
	
	def hasLogin(self):
		return self.request.session.get('retailer_login', False)
	
	def getUser(self):
		return self.request.session.get('login_retailer', None)
			 
	def logout(self):
		if self.hasLogin():
			self.request.session['retailer_login'] = None
			self.request.session['login_retailer'] = None
	
	def makeLogin(self,form):
		try:
			user = Retailer.objects.get(username = form.data['username'], password = form.data['password'])
			self.request.session['retailer_login']= True
			self.request.session['login_retailer'] = user
			return True
		except Exception,e:
			#print str(e)
			return False


#def access_required(function=None, home_url=None, redirect_field_name=None):
def retailer_access_required(function=None):
	def _dec(view_func):
		def _view(request, *args, **kwargs):
			login = RetailerLogin(request)
			if not login.hasLogin():
				return HttpResponseRedirect(reverse('retailer-login-view'))
			else:
				return view_func(request, *args, **kwargs)

		_view.__name__ = view_func.__name__
		_view.__dict__ = view_func.__dict__
		_view.__doc__ = view_func.__doc__
		return _view
	
	if function is None:
		return _dec
	else:
		return _dec(function)


def retailer_access_required_ajax(function=None):
	def _dec(view_func):
		def _view(request, *args, **kwargs):
			login = RetailerLogin(request)
			if not login.hasLogin():
				ajax = MyJson().addError('Without Login')
				return ajax.getJsonRequest()
			else:
				return view_func(request, *args, **kwargs)

		_view.__name__ = view_func.__name__
		_view.__dict__ = view_func.__dict__
		_view.__doc__ = view_func.__doc__
		return _view
	
	if function is None:
		return _dec
	else:
		return _dec(function)