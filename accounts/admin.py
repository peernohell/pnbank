from pnbank.accounts.models import Account, Transaction, Tag
from django.contrib import admin

class AccountAdmin(admin.ModelAdmin):
  list_display = ['name', 'initial_amount', 'current_amount', 'current_checked_amount']

class TransactionAdmin(admin.ModelAdmin):
  list_display = ['name', 'amount', 'date','checked']
  list_filter = ['date', 'account']
  date_hierarchy = 'date'
  
  
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Tag)
