# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

class Account(models.Model):
    name = models.CharField(max_length=100)
    initial_amount = models.FloatField(default=0.0)
    owner = models.ForeignKey(User, related_name="%(class)ss")

    def __unicode__(self):
        return self.name

    def current_amount(self):
        total_spend = Transaction.objects.filter(account = self.id)\
                .aggregate(Sum('amount'))['amount__sum'] or 0.0

        return self.initial_amount + total_spend

    def current_checked_amount(self):
        total_spend = Transaction.objects.filter(account = self.id, checked = True)\
                .aggregate(Sum('amount'))['amount__sum'] or 0.0

        return self.initial_amount + total_spend


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Transaction(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    checked = models.BooleanField(default=False)
    account = models.ForeignKey(Account, related_name="%(class)ss")
    tags = models.ManyToManyField(Tag, related_name="%(class)ss", blank=True, null=True)

    def __unicode__(self):
        return self.name

