# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UtilizadoresGrupos'
        db.create_table(u'app_utilizadoresgrupos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('utilizador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Utilizador'])),
            ('data_create', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['UtilizadoresGrupos'])

        # Adding M2M table for field amigos_grupo on 'UtilizadoresGrupos'
        db.create_table(u'app_utilizadoresgrupos_amigos_grupo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('utilizadoresgrupos', models.ForeignKey(orm[u'app.utilizadoresgrupos'], null=False)),
            ('utilizador', models.ForeignKey(orm[u'app.utilizador'], null=False))
        ))
        db.create_unique(u'app_utilizadoresgrupos_amigos_grupo', ['utilizadoresgrupos_id', 'utilizador_id'])


    def backwards(self, orm):
        # Deleting model 'UtilizadoresGrupos'
        db.delete_table(u'app_utilizadoresgrupos')

        # Removing M2M table for field amigos_grupo on 'UtilizadoresGrupos'
        db.delete_table('app_utilizadoresgrupos_amigos_grupo')


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
            'retalista': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Retalhista']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True'})
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
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'foto': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'app.utilizador': {
            'Meta': {'object_name': 'Utilizador'},
            'activa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amigos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mamigos'", 'symmetrical': 'False', 'to': u"orm['app.Utilizador']"}),
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_left': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'facebookid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'foto': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'app.utilizadoresgrupos': {
            'Meta': {'object_name': 'UtilizadoresGrupos'},
            'amigos_grupo': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'gpamigos'", 'symmetrical': 'False', 'to': u"orm['app.Utilizador']"}),
            'data_create': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utilizador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Utilizador']"})
        },
        u'app.wishlist': {
            'Meta': {'object_name': 'WishList'},
            'data_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_removed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
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