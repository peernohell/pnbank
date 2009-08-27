from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
  name = models.CharField(max_length=100)
  initial_amount = models.FloatField()
  owner = models.ForeignKey(User,related_name="accounts")
  
  def __unicode__(self):
    return self.name
    
  def current_amount(self):
    from django.db.models import Sum
    total_spend = Transaction.objects.filter(account=self.id).aggregate(Sum('amount'))['amount__sum']
    if total_spend == None:
      return self.initial_amount
    else:
      return self.initial_amount + total_spend

class Tag(models.Model):
  name = models.CharField(max_length=30)
  
  def __unicode__(self):
    return self.name

class Transaction(models.Model):
  name = models.CharField(max_length=100)
  amount = models.FloatField()
  description = models.TextField()
  date = models.DateField()
  checked = models.BooleanField(default=False)
  account = models.ForeignKey(Account)
  tags = models.ManyToManyField(Tag)
  
  def __unicode__(self):
    return self.name

