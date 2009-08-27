from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from pnbank.accounts.models import Account
# Create your views here.

@login_required
def index(request):
  accounts = Account.objects.all()
  output = ', '.join(["%s (%s)" % (t.name, t.current_amount) for t in accounts])
  return HttpResponse(output)
  
@login_required
def show(request, account_id):
  return HttpResponse("You're looking at account %s." % account_id)

