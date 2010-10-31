# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from pnbank.apps.accounts.models import Account

@login_required
def list_accounts(request):
  accounts = Account.objects.all()
  output = ', '.join(["%s (%s)" % (t.name, t.current_amount) for t in accounts])
  return HttpResponse(output)

@login_required
def view_account(request, account_id):
  return HttpResponse("You're looking at account %s." % account_id)

