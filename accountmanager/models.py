from django.db import models

class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.BigIntegerField
    routing_number = models.BigIntegerField
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return 'Account Name:'+self.name+'\nAccount Number'+\
               self.account_number+'\nRouting Number'+self.routing_number+'n'

class UtilityAccount(models.Model):
    name = models.CharField(max_length=200)
    #Number to represent occurence by month (ie, 1 = monthly 2=every second month, etc...)
    payment_frequency = models.CharField(max_length=100)
    #TODO billing history
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return 'Account Name:'+self.name+'\n'

class EntertainmentAccount(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return 'Account Name:'+self.name+'\n'

class CreditAccount(models.Model):
    name = models.CharField(max_length=200)
    credit_limit = models.FloatField
    apr = models.FloatField
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return 'Account Name:'+self.name+'\n'

class LoanAccount(models.Model):
    name = models.CharField(max_length=200)
    originating_amount = models.FloatField
    apr = models.FloatField
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return 'Account Name:'+self.name+'\n'

class RetirementAccounts(models.Model):
    name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return 'Account Name:'+self.name+'\n'