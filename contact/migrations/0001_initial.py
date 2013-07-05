# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactMessage'
        db.create_table('contact_contactmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('from_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('date_received', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_readed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('contact', ['ContactMessage'])


    def backwards(self, orm):
        # Deleting model 'ContactMessage'
        db.delete_table('contact_contactmessage')


    models = {
        'contact.contactmessage': {
            'Meta': {'object_name': 'ContactMessage'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_readed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_received': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['contact']