# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CsvTablePlugin'
        db.create_table('cmsplugin_csvtableplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('headrows', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('csv_data', self.gf('django.db.models.fields.TextField')()),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=40)),
            ('table_css', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('wrapper_css', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('cmsplugin_csvtable', ['CsvTablePlugin'])


    def backwards(self, orm):
        
        # Deleting model 'CsvTablePlugin'
        db.delete_table('cmsplugin_csvtableplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_csvtable.csvtableplugin': {
            'Meta': {'object_name': 'CsvTablePlugin', 'db_table': "'cmsplugin_csvtableplugin'", '_ormbases': ['cms.CMSPlugin']},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'csv_data': ('django.db.models.fields.TextField', [], {}),
            'headrows': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'table_css': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '40'}),
            'wrapper_css': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_csvtable']
