# -*- coding: utf-8 -*-
import json
from django.utils import simplejson
from django.http import HttpResponse


class MyJson(object):
	def __init__(self,request,*kwargs):
		super(MyJson,self).__init__(*kwargs)
		self.message = {
			'ok':None,
			'error_message':None,
			'message':None,
			'data':None,
			'flash':[],
		}
		self.request = request

	def addError(self,error):
		if self.message['error_message'] is None:
			self.message['error_message'] = []
		self.message['error_message'].append(error)
		
	def addMessage(self,message):
		self.message['message'] = message
	
	def setOk(self):
		self.message['ok'] = True
		
	def setError(self):
		self.message['ok'] = False
		
	def isError(self):
		return self.message['ok'] == False
	
	def addData(self,data):
		self.message['data'] = data
	
	def transformeJsonRequest(self,data):
		return HttpResponse(simplejson.dumps(data), mimetype='application/json')
	
	def getJsonRequest(self):
		if self.message['ok'] is None:
			self.message['ok'] = False
		if self.request.flash:
			self.message['flash'] = self.request.flash
			
		return self.transformeJsonRequest(self.message)