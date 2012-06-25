# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table('app_customuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('facebookid', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('join_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('left_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('app', ['CustomUser'])

        # Adding M2M table for field friends on 'CustomUser'
        db.create_table('app_customuser_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_customuser', models.ForeignKey(orm['app.customuser'], null=False)),
            ('to_customuser', models.ForeignKey(orm['app.customuser'], null=False))
        ))
        db.create_unique('app_customuser_friends', ['from_customuser_id', 'to_customuser_id'])

        # Adding model 'CustomUserGroup'
        db.create_table('app_customusergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.CustomUser'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('app', ['CustomUserGroup'])

        # Adding unique constraint on 'CustomUserGroup', fields ['user', 'name']
        db.create_unique('app_customusergroup', ['user_id', 'name'])

        # Adding M2M table for field friends_groups on 'CustomUserGroup'
        db.create_table('app_customusergroup_friends_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customusergroup', models.ForeignKey(orm['app.customusergroup'], null=False)),
            ('customuser', models.ForeignKey(orm['app.customuser'], null=False))
        ))
        db.create_unique('app_customusergroup_friends_groups', ['customusergroup_id', 'customuser_id'])

        # Adding model 'Retailer'
        db.create_table('app_retailer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('photo', self.gf('django.db.models.fields.URLField')(max_length=400, null=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('data_join', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('app', ['Retailer'])

        # Adding model 'Product'
        db.create_table('app_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('resume', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('app', ['Product'])

        # Adding model 'Promotion'
        db.create_table('app_promotion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Product'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=400, null=True)),
            ('retailer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Retailer'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('elements_number', self.gf('django.db.models.fields.IntegerField')()),
            ('groups_max_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('app', ['Promotion'])

        # Adding model 'PromotionGroup'
        db.create_table('app_promotiongroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promotion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='promotion', to=orm['app.Promotion'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user', to=orm['app.CustomUser'])),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('app', ['PromotionGroup'])

        # Adding model 'UserGroupPromotion'
        db.create_table('app_usergrouppromotion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.CustomUser'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.PromotionGroup'])),
            ('join_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('left_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('app', ['UserGroupPromotion'])

        # Adding model 'WishList'
        db.create_table('app_wishlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.CustomUser'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('remove_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('app', ['WishList'])

        # Adding model 'WishListProduct'
        db.create_table('app_wishlistproduct', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Product'])),
            ('wishlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.WishList'])),
            ('join_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('left_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('app', ['WishListProduct'])


    def backwards(self, orm):
        # Removing unique constraint on 'CustomUserGroup', fields ['user', 'name']
        db.delete_unique('app_customusergroup', ['user_id', 'name'])

        # Deleting model 'CustomUser'
        db.delete_table('app_customuser')

        # Removing M2M table for field friends on 'CustomUser'
        db.delete_table('app_customuser_friends')

        # Deleting model 'CustomUserGroup'
        db.delete_table('app_customusergroup')

        # Removing M2M table for field friends_groups on 'CustomUserGroup'
        db.delete_table('app_customusergroup_friends_groups')

        # Deleting model 'Retailer'
        db.delete_table('app_retailer')

        # Deleting model 'Product'
        db.delete_table('app_product')

        # Deleting model 'Promotion'
        db.delete_table('app_promotion')

        # Deleting model 'PromotionGroup'
        db.delete_table('app_promotiongroup')

        # Deleting model 'UserGroupPromotion'
        db.delete_table('app_usergrouppromotion')

        # Deleting model 'WishList'
        db.delete_table('app_wishlist')

        # Deleting model 'WishListProduct'
        db.delete_table('app_wishlistproduct')


    models = {
        'app.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'facebookid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'CustomUserFriends'", 'blank': 'True', 'to': "orm['app.CustomUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'left_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'app.customusergroup': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'CustomUserGroup'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'friends_groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'custom_user_friends_groups'", 'symmetrical': 'False', 'to': "orm['app.CustomUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.CustomUser']"})
        },
        'app.product': {
            'Meta': {'object_name': 'Product'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'resume': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'app.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elements_number': ('django.db.models.fields.IntegerField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'groups_max_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Product']"}),
            'retailer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Retailer']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True'})
        },
        'app.promotiongroup': {
            'Meta': {'object_name': 'PromotionGroup'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promotion'", 'to': "orm['app.Promotion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user'", 'to': "orm['app.CustomUser']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.CustomUser']", 'through': "orm['app.UserGroupPromotion']", 'symmetrical': 'False'})
        },
        'app.retailer': {
            'Meta': {'object_name': 'Retailer'},
            'data_join': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'app.usergrouppromotion': {
            'Meta': {'object_name': 'UserGroupPromotion'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.PromotionGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'left_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.CustomUser']"})
        },
        'app.wishlist': {
            'Meta': {'object_name': 'WishList'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Product']", 'through': "orm['app.WishListProduct']", 'symmetrical': 'False'}),
            'remove_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.CustomUser']"})
        },
        'app.wishlistproduct': {
            'Meta': {'object_name': 'WishListProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'left_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Product']"}),
            'wishlist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.WishList']"})
        }
    }

    complete_apps = ['app']