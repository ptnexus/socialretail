# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Utilizadores'
        db.create_table(u'app_utilizadores', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'app', ['Utilizadores'])


    def backwards(self, orm):
        # Deleting model 'Utilizadores'
        db.delete_table(u'app_utilizadores')


    models = {
        u'app.utilizadores': {
            'Meta': {'object_name': 'Utilizadores'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['app']