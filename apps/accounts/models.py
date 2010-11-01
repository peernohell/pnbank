# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from pnbank.externals.django_extensions.db.models import TimeStampedModel

import datetime

class Account(TimeStampedModel):
    name = models.CharField(max_length=100)
    initial_amount = models.FloatField(default=0.0)
    owner = models.ForeignKey(User, related_name="%(class)ss")

    def __unicode__(self):
        return u"%s" % self.name

    def current_amount(self):
        total_spend = Entry.objects.filter(account = self.id)\
                .aggregate(Sum('amount'))['amount__sum'] or 0.0

        return self.initial_amount + total_spend

    def current_checked_amount(self, date=datetime.date.today()):
        total_spend = Entry.objects.filter(value_date__lte=date, account = self.id, checked = True)\
                .aggregate(Sum('amount'))['amount__sum'] or 0.0

        return self.initial_amount + total_spend

class Tag(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="%(class)ss")

    def __unicode__(self):
        return u"%s" % self.name

class ThirdParty(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="thirdparties")
    tag = models.ForeignKey(Tag, related_name="thirdparties")

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = "Third Parties"

class Transaction(TimeStampedModel):
    description = models.CharField(max_length=255, blank=True, null=True)
    third_party = models.ForeignKey(ThirdParty, related_name="%(class)ss", blank=True, null=True)

    def get_amount(self):
        return self.entries.aggregate(Sum('amount'))['amount__sum'] or 0.0
    amount = property(get_amount)

    def get_value_date(self):
        try:
            return self.entries.order_by('value_date')[0].value_date
        except IndexError:
            return None
    value_date = property(get_value_date)

    def is_checked(self):
        return self.entries.filter(checked = False).count() == 0

    def __unicode__(self):
        return u"%s" % self.name

class Entry(TimeStampedModel):
    account = models.ForeignKey(Account, related_name="entries")
    transaction = models.ForeignKey(Transaction, related_name="entries")
    amount = models.FloatField()
    value_date = models.DateField()
    checked = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="entries")
    description = models.CharField(max_length=255, blank=True, null=True)

    def name(self):
        return self.transaction.name

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = "Entries"
