# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import CustomUser,CustomUserGroup
from app.forms import LoginForm
from login import RetailerLogin,retailer_access_required
from datetime import datetime
import json
from django.forms.util import ErrorList


@retailer_access_required
def home(request,*kwargs):
    return render(request, 'retailer/home.html', {},)
    #return HttpResponse(json.dumps(map(lambda x:{'name':x.nome,'email':x.email},Utilizador.objects.all())), mimetype="application/json")


def login(request,*kwargs):
    
    form = LoginForm(request.POST if request.POST else None)
    if form.is_valid():
        login = RetailerLogin(request)
        if( login.makeLogin(form) ):
            return redirect('retailer-home-view')
        else:
            errors = form._errors.setdefault("systemerror", ErrorList())
            errors.append(u'Dados de login Invalidos')
    return render(request, 'retailer/login.html', {
        'form': form, 
    },)

    
def logout(request,**kwargs):
    login = RetailerLogin(request)
    login.logout()
    return redirect('retailer-login-view')