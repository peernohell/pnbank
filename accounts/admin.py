from pnbank.accounts.models import Account, Transaction, Tag
from django.contrib import admin

class AccountAdmin(admin.ModelAdmin):
  list_display = ['name', 'initial_amount', 'current_amount']
  
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction)
admin.site.register(Tag)
