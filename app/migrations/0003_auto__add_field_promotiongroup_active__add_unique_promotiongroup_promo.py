# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PromotionGroup.active'
        db.add_column('app_promotiongroup', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding unique constraint on 'PromotionGroup', fields ['promotion', 'user']
        db.create_unique('app_promotiongroup', ['promotion_id', 'user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'PromotionGroup', fields ['promotion', 'user']
        db.delete_unique('app_promotiongroup', ['promotion_id', 'user_id'])

        # Deleting field 'PromotionGroup.active'
        db.delete_column('app_promotiongroup', 'active')


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
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'url': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        },
        'app.promotiongroup': {
            'Meta': {'unique_together': "(('user', 'promotion'),)", 'object_name': 'PromotionGroup'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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