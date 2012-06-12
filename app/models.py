from django.db import models

# Create your models here.

class Utilizadores(models.Model):
	username = models.CharField('username',max_length=80,null=False,blank=False)
	password = models.CharField('password',max_length=80,null=False,blank=False)
	email = models.EmailField('email',null=False,blank=False)
	facebookid = models.IntegerField('facebookid',null=True)
