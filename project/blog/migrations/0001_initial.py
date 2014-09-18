# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('teaser', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('model_utils.fields.StatusField')(default='draft', max_length=100, no_check_for_status=True)),
            ('published_at', self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor='status')),
        ))
        db.send_create_signal(u'blog', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'blog_article')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published_at': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "'status'"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['blog']