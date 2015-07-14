from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import BankAccount,UtilityAccount,CreditAccount,EntertainmentAccount,LoanAccount
import mintapi

email="mgshannon1s@gmail.com"
password="Fallout1"

def index(request):
    return HttpResponse("Hello, world. You're at the account manager index.")

def displayAllAccounts(request):
    bank_accounts = BankAccount.objects.order_by('-name')
    output = '\n'.join([p.name for p in bank_accounts])
    return HttpResponse(output)

def displayMintAccounts(request):
    mint = mintapi.Mint(email, password)
    output = mint.get_accounts()
    return HttpResponse(output)

def displayMintTransactions(request):
    mint = mintapi.Mint(email,password)
    output = mint.get_transactions()
    return HttpResponse(output)

def displayMintBudgets(request):
    mint = mintapi.Mint(email,password)
    output = mint.get_budgets()
    return HttpResponse(output)