# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Utilizador.nome'
        db.add_column(u'app_utilizador', 'nome',
                      self.gf('django.db.models.fields.CharField')(default='user', max_length=80),
                      keep_default=False)

        # Adding field 'Utilizador.data_nascimento'
        db.add_column(u'app_utilizador', 'data_nascimento',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Utilizador.nome'
        db.delete_column(u'app_utilizador', 'nome')

        # Deleting field 'Utilizador.data_nascimento'
        db.delete_column(u'app_utilizador', 'data_nascimento')


    models = {
        u'app.campanha': {
            'Meta': {'object_name': 'Campanha'},
            'activa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_fim': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'data_inicio': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_elementos': ('django.db.models.fields.IntegerField', [], {}),
            'numero_maximo_grupos': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'preco': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Produto']"}),
            'retalista': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Retalhista']"})
        },
        u'app.grupo': {
            'Meta': {'object_name': 'Grupo'},
            'campanha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campanha'", 'to': u"orm['app.Campanha']"}),
            'data_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utilizador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'utilizador'", 'to': u"orm['app.Utilizador']"}),
            'utilizadores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Utilizador']", 'through': u"orm['app.GrupoUtilizadores']", 'symmetrical': 'False'})
        },
        u'app.grupoutilizadores': {
            'Meta': {'object_name': 'GrupoUtilizadores'},
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_left': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grupou_grupo'", 'to': u"orm['app.Grupo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utilizador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grupou_utilizador'", 'to': u"orm['app.Utilizador']"})
        },
        u'app.produto': {
            'Meta': {'object_name': 'Produto'},
            'data_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'preco': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'resumo': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'app.retalhista': {
            'Meta': {'object_name': 'Retalhista'},
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'app.utilizador': {
            'Meta': {'object_name': 'Utilizador'},
            'activa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amigos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mamigos'", 'symmetrical': 'False', 'to': u"orm['app.Utilizador']"}),
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'facebookid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'app.wishlist': {
            'Meta': {'object_name': 'WishList'},
            'data_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_removed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produtos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Produto']", 'through': u"orm['app.WishListProdutos']", 'symmetrical': 'False'}),
            'utilizador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Utilizador']"})
        },
        u'app.wishlistprodutos': {
            'Meta': {'object_name': 'WishListProdutos'},
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_left': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'produto'", 'to': u"orm['app.Produto']"}),
            'wishlist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wishlist'", 'to': u"orm['app.WishList']"})
        }
    }

    complete_apps = ['app']