# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Utilizadores.facebookid'
        db.add_column(u'app_utilizadores', 'facebookid',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Utilizadores.facebookid'
        db.delete_column(u'app_utilizadores', 'facebookid')


    models = {
        u'app.utilizadores': {
            'Meta': {'object_name': 'Utilizadores'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'facebookid': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['app']