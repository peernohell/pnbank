# -*- coding: utf-8 -*-
""" définition des formulaires pour les produits """
from django import forms

from pnbank.apps.accounts.models import Account

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
