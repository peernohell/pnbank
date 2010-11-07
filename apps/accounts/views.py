# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.db.models import Min
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.create_update import create_object, update_object, delete_object
from django.views.generic.list_detail import object_detail, object_list

from pnbank.apps.accounts.models import Account, Entry, Transaction
from pnbank.apps.accounts.forms import get_account_form, get_entry_form

from pnbank.externals.qsstats import QuerySetStats

@permission_required('accounts.list_account')
def list_accounts(request):
    qss = None
    qs = Account.objects.filter(owner = request.user)

    if qs:
        qss = QuerySetStats(qs, 'created')

    return object_list(
        request = request,
        queryset = qs,
        template_name = 'account_list.html',
        allow_empty = True,
        extra_context = {
            'qss': qss,
        }
    )

@permission_required('accounts.add_account')
def create_account(request):
    return create_object(
        request,
        form_class = get_account_form(request),
        post_save_redirect = reverse('list_accounts'),
        template_name = 'account_form.html',
    )

@permission_required('accounts.change_account')
def update_account(request, account_id):
    if not request.user.is_superuser:
        get_object_or_404(Account, owner=request.user, pk=account_id)
    else:
        get_object_or_404(Account, pk=account_id)

    return update_object(
        request,
        form_class = get_account_form(request),
        post_save_redirect = reverse('view_account', kwargs={'account_id': account_id}),
        object_id = account_id,
        template_name = 'account_form.html',
    )

@permission_required('accounts.view_account')
def view_account(request, account_id):
    if not request.user.is_superuser:
        get_object_or_404(Account, owner=request.user, pk=account_id)
    else:
        get_object_or_404(Account, pk=account_id)

    qss_entries = None
    qss_transactions = None
    qs = Account.objects.filter(pk = account_id)
    transaction_qs = Transaction.objects.filter(entries__account = account_id)\
            .annotate(date=Min('entries__date'))

    if qs:
        qss_entries = QuerySetStats(qs, 'entries__date')
        qss_transactions = QuerySetStats(transaction_qs, 'date')

    return object_detail(
        request = request,
        queryset = qs,
        object_id = account_id,
        template_name = "account_detail.html",
        extra_context = {
            'qss_entries': qss_entries,
            'qss_transactions': qss_transactions,
        }
    )

@permission_required("accounts.delete_account")
def delete_account(request, account_id):
    if not request.user.is_superuser:
        get_object_or_404(Account, owner=request.user, pk=account_id)
    else:
        get_object_or_404(Account, pk=account_id)

    reverse_url = reverse('list_accounts')

    return delete_object(
        request = request,
        object_id = account_id,
        post_delete_redirect = reverse_url,
        model = Account,
        template_name = 'confirm_delete.html',
        extra_context = {
            'object_name': Account._meta.verbose_name.lower(),
            'redirect': reverse_url,
        }
    )

@permission_required('accounts.list_entry')
def list_entries(request, account_id=None):
    qs = Entry.objects.filter(account__owner = request.user)

    if account_id:
        account = get_object_or_404(Account, pk=account_id)
        qs = qs.filter(account = account)
        extra_context = {
            'account': account,
        }
    else:
        extra_context = {}


    return object_list(
        request = request,
        queryset = qs,
        template_name = 'entry_list.html',
        allow_empty = True,
        extra_context = extra_context,
    )

@permission_required('accounts.add_entry')
def create_entry(request, account_id=None):
    if account_id:
        account = get_object_or_404(Account, pk=account_id)
        reverse_url = reverse('list_entries', kwargs={'account_id': account_id})
        extra_context = {
            'account': account,
        }
    else:
        reverse_url = reverse('list_entries')
        extra_context = {}

    return create_object(
        request,
        form_class = get_entry_form(request, account_id),
        post_save_redirect = reverse_url,
        template_name = 'entry_form.html',
        extra_context = extra_context,
    )

@permission_required('accounts.change_entry')
def update_entry(request, entry_id, account_id=None):
    if not request.user.is_superuser:
        entry = get_object_or_404(Entry, owner=request.user, pk=entry_id)
    else:
        entry = get_object_or_404(Entry, pk=entry_id)

    if account_id:
        account = get_object_or_404(Account, pk=account_id)
        if entry.account != account:
            raise Http404

        reverse_url = reverse('view_entry', kwargs={
            'entry_id': entry_id,
            'account_id': account_id,
        })
        extra_context = {
            'account': account,
        }
    else:
        reverse_url = reverse('view_entry', kwargs={'entry_id': entry_id})
        extra_context = {}

    return update_object(
        request,
        form_class = get_entry_form(request, account_id),
        post_save_redirect = reverse_url,
        object_id = entry_id,
        template_name = 'entry_form.html',
        extra_context = extra_context,
    )

@permission_required('accounts.view_entry')
def view_entry(request, entry_id, account_id=None):
    if not request.user.is_superuser:
        entry = get_object_or_404(Entry, owner=request.user, pk=entry_id)
    else:
        entry = get_object_or_404(Entry, pk=entry_id)

    if account_id:
        account = get_object_or_404(Account, pk=account_id)
        if entry.account != account:
            raise Http404

        extra_context = {
            'account': account,
        }
    else:
        extra_context = {}

    qs = Entry.objects.filter(pk = entry_id)

    return object_detail(
        request = request,
        queryset = qs,
        object_id = entry_id,
        template_name = "entry_detail.html",
        extra_context = extra_context,
    )

@permission_required("accounts.delete_entry")
def delete_entry(request, entry_id, account_id=None):
    if not request.user.is_superuser:
        get_object_or_404(Entry, owner=request.user, pk=entry_id)
    else:
        get_object_or_404(Entry, pk=entry_id)

    if account_id:
        account = get_object_or_404(Account, pk=account_id)
        reverse_url = reverse('list_entries', kwargs={'account_id': account_id})
        extra_context = {
            'account': account,
        }
    else:
        reverse_url = reverse('list_entries')
        extra_context = {}

    extra_context.update({'redirect': reverse_url})

    return delete_object(
        request = request,
        object_id = entry_id,
        post_delete_redirect = reverse_url,
        model = Entry,
        template_name = 'confirm_delete.html',
        extra_context = extra_context,
    )

