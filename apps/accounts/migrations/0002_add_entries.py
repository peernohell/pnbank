# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Entry'
        db.create_table('accounts_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('value_date', self.gf('django.db.models.fields.DateField')()),
            ('checked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Account'])),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Transaction'])),
        ))
        db.send_create_signal('accounts', ['Entry'])

        # Adding M2M table for field tags on 'Entry'
        db.create_table('accounts_entry_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['accounts.entry'], null=False)),
            ('tag', models.ForeignKey(orm['accounts.tag'], null=False))
        ))
        db.create_unique('accounts_entry_tags', ['entry_id', 'tag_id'])

        # Deleting field 'Transaction.account'
        db.delete_column('accounts_transaction', 'account_id')

        # Deleting field 'Transaction.checked'
        db.delete_column('accounts_transaction', 'checked')

        # Deleting field 'Transaction.amount'
        db.delete_column('accounts_transaction', 'amount')

        # Removing M2M table for field tags on 'Transaction'
        db.delete_table('accounts_transaction_tags')


    def backwards(self, orm):
        
        # Deleting model 'Entry'
        db.delete_table('accounts_entry')

        # Removing M2M table for field tags on 'Entry'
        db.delete_table('accounts_entry_tags')

        # Adding field 'Transaction.account'
        db.add_column('accounts_transaction', 'account', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='transactions', to=orm['accounts.Account']), keep_default=False)

        # Adding field 'Transaction.checked'
        db.add_column('accounts_transaction', 'checked', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Transaction.amount'
        db.add_column('accounts_transaction', 'amount', self.gf('django.db.models.fields.FloatField')(default=None), keep_default=False)

        # Adding M2M table for field tags on 'Transaction'
        db.create_table('accounts_transaction_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('transaction', models.ForeignKey(orm['accounts.transaction'], null=False)),
            ('tag', models.ForeignKey(orm['accounts.tag'], null=False))
        ))
        db.create_unique('accounts_transaction_tags', ['transaction_id', 'tag_id'])


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
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']"}),
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['accounts.Tag']", 'symmetrical': 'False'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Transaction']"}),
            'value_date': ('django.db.models.fields.DateField', [], {})
        },
        'accounts.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'accounts.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
