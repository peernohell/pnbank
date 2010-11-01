# -*- coding: utf-8 -*-
from django.contrib import admin
from pnbank.apps.accounts.models import Account, Transaction, Tag, Entry

class AccountAdmin(admin.ModelAdmin):
  list_display = ['name', 'initial_amount', 'current_amount', 'current_checked_amount']

class EntryAdmin(admin.ModelAdmin):
  list_display = ['name', 'amount', 'date', 'value_date','checked']
  list_filter = ['date', 'value_date', 'account']
  date_hierarchy = 'date'

class EntryInline(admin.TabularInline):
  model = Entry 
  raw_id_fields = ("tags",)

  
class TransactionAdmin(admin.ModelAdmin):
  list_display = ['name', 'amount', 'date']
  inlines =  [ EntryInline, ]
  exclude = ('date',)

  def save_model(self, request, obj, form, change):
    import datetime
    obj.date = datetime.date(1900,01,01)
    obj.save()

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
