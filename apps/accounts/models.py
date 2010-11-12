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
    owner = models.ForeignKey(User, related_name="%(class)ss", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

class ThirdParty(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="thirdparties")
    tag = models.ForeignKey(Tag, related_name="thirdparties", null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name_plural = "thirdparties"

class Transaction(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)

    @property
    def amount(self):
        return self.entries.aggregate(Sum('amount'))['amount__sum'] or 0.0

    @property
    def value_date(self):
        try:
            return self.entries.order_by('value_date')[0].value_date
        except IndexError:
            return None

    def is_checked(self):
        return self.entries.filter(checked = False).count() == 0

    def __unicode__(self):
        return u"%s" % self.description

class Entry(models.Model):
    account = models.ForeignKey(Account, related_name="entries")
    transaction = models.ForeignKey(Transaction, related_name="entries")
    third_party = models.ForeignKey(ThirdParty, related_name="entries", blank=True, null=True)
    amount = models.FloatField()
    date = models.DateField()
    value_date = models.DateField(blank=True, null=True)
    checked = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="entries", blank=True, null=True)

    def name(self):
        return self.third_party.name

    def __unicode__(self):
        return u"Entry #%d" % self.pk

    class Meta:
        verbose_name_plural = "entries"
        ordering = ['-date']

