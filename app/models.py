# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Utilizador(models.Model):
	username = models.CharField('username',max_length=80,null=False,blank=False)
	password = models.CharField('password',max_length=80,null=False,blank=False)
	email = models.EmailField('email',null=False,blank=False)
	facebookid = models.IntegerField('facebookid',null=True)
	data_join = models.DateTimeField(u'data join',auto_now_add=True,null=False)
	

class Retalhista(models.Model):
	username = models.CharField('username',max_length=80,null=False,blank=False)
	password = models.CharField('password',max_length=80,null=False,blank=False)
	email = models.EmailField('email',null=False,blank=False)
	data_join = models.DateTimeField(u'data join',auto_now_add=True,null=False)
	

class Produto(models.Model):
	nome = models.CharField('nome',max_length=80,null=False,blank=False)
	resumo = models.CharField('resumo',max_length=80,null=False,blank=False)
	descricao = models.TextField('descricao',null=False,blank=False)
	data_created = models.DateTimeField(u'data criação',auto_now_add=True,null=False)
	
	
class Campanha(models.Model):
	produto = models.ForeignKey(Produto,null=False)
	retalista = models.ForeignKey(Retalhista,null=False)
	preco = models.DecimalField('preco',decimal_places=2,max_digits=12,null=False)
	data_inicio = models.DateTimeField('data inicio',auto_now=True,null=False)
	data_fim = models.DateTimeField('data fim',null=True)
	data_created = models.DateTimeField(u'data criação',auto_now_add=True,null=False)
	numero_elementos = models.IntegerField(u'numero elementos',null=False)
	numero_maximo_grupos = models.IntegerField(u'numero maximo de grupos',null=True) 
	activa = models.BooleanField('activo',default=True)
	
class Grupo(models.Model):
	campanha = models.ForeignKey(Campanha,null=False,related_name='campanha')
	utilizador = models.ForeignKey(Utilizador,null=False,related_name='utilizador') 
	data_created = models.DateTimeField(u'data criação',auto_now_add=True,null=False)
	utilizadores = models.ManyToManyField(Utilizador,through='GrupoUtilizadores')


class GrupoUtilizadores(models.Model):
	utilizador = models.ForeignKey(Utilizador,related_name='grupou_utilizador')
	grupo = models.ForeignKey(Grupo,related_name='grupou_grupo')
	data_join = models.DateTimeField(u'data join',auto_now_add=True,null=False)
	data_left = models.DateTimeField(u'data left',null=True)
    
	
	
	