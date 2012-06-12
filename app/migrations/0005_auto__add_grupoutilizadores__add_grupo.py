# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GrupoUtilizadores'
        db.create_table(u'app_grupoutilizadores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('utilizador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='utilizador_grupo', to=orm['app.Utilizador'])),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='grupo_utilizador', to=orm['app.Grupo'])),
            ('data_join', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_left', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal(u'app', ['GrupoUtilizadores'])

        # Adding model 'Grupo'
        db.create_table(u'app_grupo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campanha', self.gf('django.db.models.fields.related.ForeignKey')(related_name='campanha', to=orm['app.Campanha'])),
            ('utilizador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='utilizador', to=orm['app.Utilizador'])),
            ('data_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Grupo'])


    def backwards(self, orm):
        # Deleting model 'GrupoUtilizadores'
        db.delete_table(u'app_grupoutilizadores')

        # Deleting model 'Grupo'
        db.delete_table(u'app_grupo')


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
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'grupo_utilizador'", 'to': u"orm['app.Grupo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'utilizador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'utilizador_grupo'", 'to': u"orm['app.Utilizador']"})
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