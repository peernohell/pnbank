# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.db.models import Min
from django.shortcuts import get_object_or_404
from django.views.generic.create_update import create_object, update_object, delete_object
from django.views.generic.list_detail import object_detail, object_list

from pnbank.apps.accounts.models import Account, Transaction
from pnbank.apps.accounts.forms import get_account_form

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
        get_object_or_404( Account, owner=request.user, pk=account_id)
    else:
        get_object_or_404( Account, pk=account_id)

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
        get_object_or_404( Account, owner=request.user, pk=account_id)
    else:
        get_object_or_404( Account, pk=account_id)

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
        get_object_or_404( Account, owner=request.user, pk=account_id)
    else:
        get_object_or_404( Account, pk=account_id)

    return delete_object(
        request = request,
        object_id = account_id,
        post_delete_redirect = reverse('list_accounts'),
        model = Account,
        template_name = 'confirm_delete.html',
        extra_context = {
            'object_name': Account._meta.verbose_name.lower(),
        }
    )

