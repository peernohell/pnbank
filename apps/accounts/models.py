# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
import datetime

class Account(models.Model):
    name = models.CharField(max_length=100)
    initial_amount = models.FloatField(default=0.0)
    owner = models.ForeignKey(User, related_name="%(class)ss")

    def __unicode__(self):
        return self.name

    def current_amount(self):
        total_spend = Entry.objects.filter(account = self.id)\
                .aggregate(Sum('amount'))['amount__sum'] or 0.0

        return self.initial_amount + total_spend

    def current_checked_amount(self, date=datetime.date.today()):
        total_spend = Entry.objects.filter(value_date__lte=date, account = self.id, checked = True)\
                .aggregate(Sum('amount'))['amount__sum'] or 0.0

        return self.initial_amount + total_spend


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Transaction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

	def amount(self):
		from django.db.models import Sum
		amount = Entry.objects.filter(transaction=self.pk).aggregate(Sum('amount'))['amount__sum']
		return amount == None and 0 or amount

	def oldestEntry(self):
		from datetime import date
		return Entry.objects.filter(transaction=self.pk).order_by('date')[0]

	def updateDate(self):
		if(self.date != self.oldestEntry().date):
			self.date = self.oldestEntry().date
			self.save()

    def __unicode__(self):
        return self.name

class Entry(models.Model):
	amount = models.FloatField()
	date = models.DateField()
	value_date = models.DateField()
	checked = models.BooleanField(default=False)
	account = models.ForeignKey(Account)
	transaction = models.ForeignKey(Transaction)
	tags = models.ManyToManyField(Tag)

	def name(self):
		return self.transaction.name

	def __unicode__(self):
		return self.name()

def updateTransactionDate(sender, **kwargs):
	import datetime
	kwargs['instance'].transaction.updateDate()

models.signals.post_save.connect(updateTransactionDate, sender=Entry)

