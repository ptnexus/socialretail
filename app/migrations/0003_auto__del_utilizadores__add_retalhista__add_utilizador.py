# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Utilizadores'
        db.delete_table(u'app_utilizadores')

        # Adding model 'Retalhista'
        db.create_table(u'app_retalhista', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'app', ['Retalhista'])

        # Adding model 'Utilizador'
        db.create_table(u'app_utilizador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('facebookid', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'app', ['Utilizador'])


    def backwards(self, orm):
        # Adding model 'Utilizadores'
        db.create_table(u'app_utilizadores', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebookid', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'app', ['Utilizadores'])

        # Deleting model 'Retalhista'
        db.delete_table(u'app_retalhista')

        # Deleting model 'Utilizador'
        db.delete_table(u'app_utilizador')


    models = {
        u'app.retalhista': {
            'Meta': {'object_name': 'Retalhista'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'app.utilizador': {
            'Meta': {'object_name': 'Utilizador'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'facebookid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['app']