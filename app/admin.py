# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Utilizador,Retalhista,Produto,Campanha
from models import Grupo,GrupoUtilizadores,WishList,WishListProdutos

class UtilizadorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Utilizador, UtilizadorAdmin)


class RetalhistaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Retalhista, RetalhistaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Produto, ProdutoAdmin)

class CampanhaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Campanha, CampanhaAdmin)

class GrupoUtilizadoresInline(admin.TabularInline):
	model = GrupoUtilizadores

class GrupoAdmin(admin.ModelAdmin):
    inlines = [
    	GrupoUtilizadoresInline
    ]
admin.site.register(Grupo, GrupoAdmin)


class WishListProdutosInline(admin.TabularInline):
    model = WishListProdutos

class WishListAdmin(admin.ModelAdmin):
    inlines = [
    	WishListProdutosInline
    ]
    
admin.site.register(WishList, WishListAdmin)



