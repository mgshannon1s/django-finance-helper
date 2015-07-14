__author__ = 'mike'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/$', views.displayAllAccounts, name='accounts'),
    url(r'^accounts/mint/$', views.displayMintAccounts, name='mint accounts'),
    url(r'^accounts/mint/transactions$', views.displayMintTransactions, name='mint transactions'),
    url(r'^accounts/mint/$', views.displayMintBudgets, name='mint budgets'),
]
