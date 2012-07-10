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


class PromotionGroupAdmin(admin.ModelAdmin):
	pass

admin.site.register(PromotionGroup, PromotionGroupAdmin)


class WishListAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(WishList, WishListAdmin)



