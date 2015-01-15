# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Question.slug'
        db.add_column(u'blog_question', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='ho', max_length=54),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Question.slug'
        db.delete_column(u'blog_question', 'slug')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published_at': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "'status'"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'blog.question': {
            'Meta': {'object_name': 'Question'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'published_at': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "'status'"}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '54'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['blog']