from django.db import models

class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class UtilityAccount(models.Model):
    name = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class EntertainmentAccount(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class CreditAccount(models.Model):
    name = models.CharField(max_length=200)
    credit_limit = models.FloatField
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class LoanAccount(models.Model):
    name = models.CharField(max_length=200)
    originating_amount = models.FloatField
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.name
