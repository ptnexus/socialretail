# -*- coding: utf-8 -*-
from django.contrib import admin


from models import *

class CustomUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomUser, CustomUserAdmin)

"""
class GrupoUtilizadoresInline(admin.TabularInline):
	model = GrupoUtilizadores
"""
class CustomUserGroupAdmin(admin.ModelAdmin):
	pass
	"""
    inlines = [
    	UtilizadoresGruposInline
    ]
    """
admin.site.register(CustomUserGroup, CustomUserGroupAdmin)



class RetailerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Retailer, RetailerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class PromotionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Promotion, PromotionAdmin)

"""
class GrupoUtilizadoresInline(admin.TabularInline):
	model = GrupoUtilizadores

class GrupoAdmin(admin.ModelAdmin):
    inlines = [
    	GrupoUtilizadoresInline
    ]
admin.site.register(Grupo, GrupoAdmin)
"""

class UserGroupPromotionInline(admin.TabularInline):
	model = UserGroupPromotion

class PromotionGroupAdmin(admin.ModelAdmin):
	inlines = [
    	UserGroupPromotionInline
    ]

admin.site.register(PromotionGroup, PromotionGroupAdmin)



class WishListProductInline(admin.TabularInline):
    model = WishListProduct

class WishListAdmin(admin.ModelAdmin):
    inlines = [
    	WishListProductInline
    ]
    
admin.site.register(WishList, WishListAdmin)



