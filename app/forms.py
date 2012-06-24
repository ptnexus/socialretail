# -*- coding: utf-8 -*-
from app.models import Utilizador,UtilizadoresGrupos
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100, widget=forms.TextInput(
    	attrs = { 'class':"input-medium", 'placeholder':"Username" }
    ))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(
    	attrs = { 'class':"input-small", 'placeholder':"Password" }
    ))
    remember = forms.BooleanField(required=False)
    
class UtilizadoresGruposForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
	    super (UtilizadoresGruposForm, self).__init__(*args, **kwargs)
	    #self.fields['topics'].queryset = Topic.objects.filter(event=event)
	    self.fields['amigos_grupo'].widget.attrs['class'] = "multiselect"
	    self.fields['amigos_grupo'].widget.attrs['style'] = "width:440px;height:250px;"
	#amigos_grupo = forms.ModelMultipleChoiceField(queryset=Utilizador.objects)
	class Meta:
		model = UtilizadoresGrupos
		exclude = ('utilizador',)