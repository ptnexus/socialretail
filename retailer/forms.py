# -*- coding: utf-8 -*-
from app.models import CustomUser,CustomUserGroup,WishList
from django import forms
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100, widget=forms.TextInput(
    	attrs = { 'class':"input-medium", 'placeholder':"Username" }
    ))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(
    	attrs = { 'class':"input-small", 'placeholder':"Password" }
    ))
    remember = forms.BooleanField(required=False)
    
class CustomUserGroupForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    super (CustomUserGroupForm, self).__init__(*args, **kwargs)
	    self.fields['friends_groups'].widget.attrs['class'] = "multiselect"
	    self.fields['friends_groups'].widget.attrs['style'] = "width:440px;height:250px;"
	
	#friends_groups = forms.ModelMultipleChoiceField(queryset=Utilizador.objects,)
	def validate_unique(self):
		exclude = self._get_validation_exclusions()
		exclude.remove('user') # allow checking against the missing attribute
		try:
			self.instance.validate_unique(exclude=exclude)
		except ValidationError, e:
			self._update_errors(e.message_dict)
	class Meta:
		model = CustomUserGroup
		exclude = ('user',)
		
class WishListProductForm(forms.ModelForm):
	def validate_unique(self):
		exclude = self._get_validation_exclusions()
		exclude.remove('user') # allow checking against the missing attribute
		try:
			self.instance.validate_unique(exclude=exclude)
		except ValidationError, e:
			self._update_errors(e.message_dict)
	class Meta:
		model = WishList
		exclude = ('remove_date','user','products')
		
class WishListForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    super (WishListForm, self).__init__(*args, **kwargs)
	    self.fields['products'].widget.attrs['class'] = "multiselect"
	    self.fields['products'].widget.attrs['style'] = "width:440px;height:250px;"
	    
	def validate_unique(self):
		exclude = self._get_validation_exclusions()
		exclude.remove('user') # allow checking against the missing attribute
		try:
			self.instance.validate_unique(exclude=exclude)
		except ValidationError, e:
			self._update_errors(e.message_dict)
	class Meta:
		model = WishList
		exclude = ('remove_date','user',)