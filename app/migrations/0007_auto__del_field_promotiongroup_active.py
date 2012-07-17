# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PromotionGroup.active'
        db.delete_column('app_promotiongroup', 'active')


    def backwards(self, orm):
        # Adding field 'PromotionGroup.active'
        db.add_column('app_promotiongroup', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    models = {
        'app.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'facebookid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
        'app.inviteuserpromotion': {
            'Meta': {'object_name': 'InviteUserPromotion'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.PromotionGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Messages']"}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Promotion']"}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invite_user_from'", 'to': "orm['app.CustomUser']"}),
            'user_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invite_user_to'", 'to': "orm['app.CustomUser']"})
        },
        'app.messages': {
            'Meta': {'object_name': 'Messages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'read_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_from': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_from'", 'to': "orm['app.CustomUser']"}),
            'user_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_to'", 'to': "orm['app.CustomUser']"})
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
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promotionGroups'", 'to': "orm['app.Promotion']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user'", 'to': "orm['app.CustomUser']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'promotion_group_users'", 'symmetrical': 'False', 'to': "orm['app.CustomUser']"}),
            'win_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
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
        'app.wishlist': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'WishList'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'wishlist_product'", 'symmetrical': 'False', 'to': "orm['app.Product']"}),
            'remove_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.CustomUser']"})
        }
    }

    complete_apps = ['app']