# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class CustomUserManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT p.id, p.question, p.poll_date, COUNT(*)
            FROM polls_opinionpoll p, polls_response r
            WHERE p.id = r.poll_id
            GROUP BY 1, 2, 3
            ORDER BY 3 DESC""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(id=row[0], question=row[1], poll_date=row[2])
            p.num_responses = row[3]
            result_list.append(p)
        return result_list

class CustomUser(models.Model):
	username = models.CharField('username',max_length=80,null=False,blank=False,unique=True)
	password = models.CharField('password',max_length=80,null=False,blank=False)
	email = models.EmailField('email',null=False,blank=False,unique=True)
	facebookid = models.IntegerField('facebookid',null=True,unique=True)
	name = models.CharField('name',max_length=80,null=False,blank=False)
	birth_date = models.DateField(u'birth date',null=False)
	join_date = models.DateTimeField(u'join date',auto_now_add=True,null=False)
	left_date = models.DateTimeField(u'left date',null=True,blank=True)
	active = models.BooleanField('active',default=True)
	friends = models.ManyToManyField('CustomUser',related_name='CustomUserFriends',blank=True)
	photo = models.URLField('photo',null=True,blank=True)
	def __unicode__(self):
		return self.name
	def getTable(self):
		return "<tr><td>"+self.name+"</td><td>"+self.email+"</td></tr>"
	
class CustomUserGroup(models.Model):
	user = models.ForeignKey(CustomUser,null=False)
	name = models.CharField('name',max_length=80,null=False,blank=False)
	create_date = models.DateTimeField(u'create date',auto_now_add=True,null=False)
	friends_groups = models.ManyToManyField('CustomUser',related_name='custom_user_friends_groups')
	class Meta:
		unique_together = ( ('user','name'),)
	
class Retailer(models.Model):
	username = models.CharField('username',max_length=80,null=False,blank=False,unique=True)
	password = models.CharField('password',max_length=80,null=False,blank=False)
	email = models.EmailField('email',null=False,blank=False,unique=True)
	
	photo = models.URLField('photo',max_length=400,null=True)
	url = models.URLField('link',max_length=400,null=True)
	name = models.CharField('name',max_length=80,null=False,blank=False)
	description = models.TextField('description',null=True,blank=False)
	data_join = models.DateTimeField(u'data join',auto_now_add=True,null=False)
	

class Product(models.Model):
	name = models.CharField('name',max_length=80,null=False,blank=False)
	resume = models.CharField('resume',max_length=80,null=False,blank=False)
	price = models.DecimalField('price',decimal_places=2,max_digits=12,null=False)
	description = models.TextField('description',null=False,blank=False)
	create_date = models.DateTimeField(u'create date',auto_now_add=True,null=False)
	photo = models.URLField('photo',null=True,blank=True)
	def formattedprice(self):
		return "€%01.2f" % self.price
	def __unicode__(self):
		return self.name
	
	
class Promotion(models.Model):
	product = models.ForeignKey(Product,null=False)
	url = models.URLField('link',max_length=400,null=True,blank=True)
	retailer = models.ForeignKey(Retailer,null=False)
	price = models.DecimalField('price',decimal_places=2,max_digits=12,null=False)
	start_date = models.DateTimeField('start date',auto_now=True,null=False)
	end_date = models.DateTimeField('end date',null=True)
	create_date = models.DateTimeField(u'create date',auto_now_add=True,null=False)
	elements_number = models.IntegerField(u'elements number',null=False)
	groups_max_number = models.IntegerField(u'groups max number',null=True) 
	active = models.BooleanField('active',default=True)
	def formattedprice(self):
		return "€%01.2f" % self.price
	def userInPromotion(self,myuser):
		for p in PromotionGroup.objects.filter(promotion=self,active=True).prefetch_related('users'):
			if p.users.filter(user=myuser,).count() > 0:
				return True
		return False
		
	def getPromotionInfo(self,user):
		return {
			'promotion': self,
			'join':self.userInPromotion(user),
		}
	
class PromotionGroup(models.Model):
	promotion = models.ForeignKey(Promotion,null=False,related_name='promotion')
	user = models.ForeignKey(CustomUser,null=False,related_name='user') 
	create_date = models.DateTimeField(u'create date',auto_now_add=True,null=False)
	#users = models.ManyToManyField(CustomUser,through='UserGroupPromotion')
	users = models.ManyToManyField(CustomUser,related_name='promotion_group_users')
	active = models.BooleanField('active',default=True)
	class Meta:
		unique_together = ( ('user','promotion'),)

	
class WishList(models.Model):
	user = models.ForeignKey(CustomUser,)
	name = models.CharField('name',max_length=80,null=False,blank=False)
	create_date = models.DateTimeField(u'create date',auto_now_add=True,null=False)
	remove_date = models.DateTimeField(u'remove date',null=True,blank=True)
	#products = models.ManyToManyField(Product,through='WishListProduct', related_name='wishlist_product')
	products = models.ManyToManyField(Product, related_name='wishlist_product')
	class Meta:
		unique_together = ( ('user','name'),)

	
	
	