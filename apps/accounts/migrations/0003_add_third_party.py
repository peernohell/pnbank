# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'ThirdParty'
        db.create_table('accounts_thirdparty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='thirdparties', to=orm['auth.User'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(related_name='thirdparties', to=orm['accounts.Tag'])),
        ))
        db.send_create_signal('accounts', ['ThirdParty'])

        # Deleting field 'Transaction.date'
        db.delete_column('accounts_transaction', 'date')

        # Deleting field 'Transaction.name'
        db.delete_column('accounts_transaction', 'name')

        # Adding field 'Transaction.third_party'
        db.add_column('accounts_transaction', 'third_party', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='transactions', null=True, to=orm['accounts.ThirdParty']), keep_default=False)

        # Changing field 'Transaction.description'
        db.alter_column('accounts_transaction', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Adding field 'Entry.description'
        db.add_column('accounts_entry', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Tag.owner'
        db.add_column('accounts_tag', 'owner', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='tags', to=orm['auth.User']), keep_default=False)

        # Changing field 'Tag.name'
        db.alter_column('accounts_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):

        # Deleting model 'ThirdParty'
        db.delete_table('accounts_thirdparty')

        # Adding field 'Transaction.date'
        db.add_column('accounts_transaction', 'date', self.gf('django.db.models.fields.DateField')(default=None), keep_default=False)

        # Adding field 'Transaction.name'
        db.add_column('accounts_transaction', 'name', self.gf('django.db.models.fields.CharField')(default=None, max_length=100), keep_default=False)

        # Deleting field 'Transaction.third_party'
        db.delete_column('accounts_transaction', 'third_party_id')

        # Changing field 'Transaction.description'
        db.alter_column('accounts_transaction', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Deleting field 'Entry.description'
        db.delete_column('accounts_entry', 'description')

        # Deleting field 'Tag.owner'
        db.delete_column('accounts_tag', 'owner_id')

        # Changing field 'Tag.name'
        db.alter_column('accounts_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))


    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_amount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accounts'", 'to': "orm['auth.User']"})
        },
        'accounts.entry': {
            'Meta': {'object_name': 'Entry'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['accounts.Account']"}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'entries'", 'symmetrical': 'False', 'to': "orm['accounts.Tag']"}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['accounts.Transaction']"}),
            'value_date': ('django.db.models.fields.DateField', [], {})
        },
        'accounts.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': "orm['auth.User']"})
        },
        'accounts.thirdparty': {
            'Meta': {'object_name': 'ThirdParty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thirdparties'", 'to': "orm['auth.User']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thirdparties'", 'to': "orm['accounts.Tag']"})
        },
        'accounts.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'third_party': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'transactions'", 'null': 'True', 'to': "orm['accounts.ThirdParty']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']
