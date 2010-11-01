# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from pnbank.apps.accounts.models import Account
from pnbank.externals.qsstats import QuerySetStats

import datetime

@login_required
def list_accounts(request):
    accounts = Account.objects.all()
    output = ', '.join(["%s (%s)" % (t.name, t.current_amount) for t in accounts])

    qs = User.objects.all()
    qss = QuerySetStats(qs, 'date_joined')

    output += '%s new accounts today.<br/>' % qss.this_day()
    output += '%s new accounts this month.<br/>' % qss.this_month()
    output += '%s new accounts this year.<br/>' % qss.this_year()
    output += '%s new accounts until now.<br/>' % qss.until_now()


    today = datetime.date.today()
    seven_days_ago = today - datetime.timedelta(days=7)

    time_series = qss.time_series(seven_days_ago, today)
    output += 'New users in the last 7 days: %s<br />' % [t[1] for t in time_series]

    return render_to_response(
        "account_list.html",
        {
            'output': output,
        },
        context_instance = RequestContext(request)
    )

@login_required
def view_account(request, account_id):
  return HttpResponse("You're looking at account %s." % account_id)

