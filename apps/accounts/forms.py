# -*- coding: utf-8 -*-
""" définition des formulaires pour les produits """
from django import forms

from pnbank.apps.accounts.models import Account, Entry
from pnbank.forms.widgets import DatePickerInput

def get_account_form(request):
    class AccountForm(forms.ModelForm):

        def save(self, commit=True):
            instance = super(AccountForm, self).save(commit=False)

            if not getattr(instance, 'owner_id', None):
                instance.owner = request.user

            if commit and self.is_valid():
                instance.save()
                self.save_m2m()

            return instance

        class Meta:
            model = Account
            exclude = ['owner']

    return AccountForm

def get_entry_form(request, account_id=None):
    class EntryForm(forms.ModelForm):
        date = forms.DateField(
            widget = DatePickerInput,
            required = True,
        )
        value_date = forms.DateField(
            widget = DatePickerInput,
            required = False,
        )

        def save(self, commit=True):
            instance = super(EntryForm, self).save(commit=False)

            if not getattr(instance, 'account_id', None):
                instance.account = Account.objects.get(pk=account_id)

            if commit and self.is_valid():
                instance.save()
                self.save_m2m()

            return instance

        class Meta:
            model = Entry

            if account_id:
                exclude = ['account']

    return EntryForm
