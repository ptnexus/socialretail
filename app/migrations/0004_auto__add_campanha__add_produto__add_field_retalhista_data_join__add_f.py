# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campanha'
        db.create_table(u'app_campanha', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Produto'])),
            ('retalista', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Retalhista'])),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('data_inicio', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('data_fim', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('data_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('numero_elementos', self.gf('django.db.models.fields.IntegerField')()),
            ('numero_maximo_grupos', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'app', ['Campanha'])

        # Adding model 'Produto'
        db.create_table(u'app_produto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('resumo', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('data_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Produto'])

        # Adding field 'Retalhista.data_join'
        db.add_column(u'app_retalhista', 'data_join',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 6, 12, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Utilizador.data_join'
        db.add_column(u'app_utilizador', 'data_join',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 6, 12, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Campanha'
        db.delete_table(u'app_campanha')

        # Deleting model 'Produto'
        db.delete_table(u'app_produto')

        # Deleting field 'Retalhista.data_join'
        db.delete_column(u'app_retalhista', 'data_join')

        # Deleting field 'Utilizador.data_join'
        db.delete_column(u'app_utilizador', 'data_join')


    models = {
        u'app.campanha': {
            'Meta': {'object_name': 'Campanha'},
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
        u'app.produto': {
            'Meta': {'object_name': 'Produto'},
            'data_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'resumo': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'app.retalhista': {
            'Meta': {'object_name': 'Retalhista'},
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'app.utilizador': {
            'Meta': {'object_name': 'Utilizador'},
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'facebookid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['app']