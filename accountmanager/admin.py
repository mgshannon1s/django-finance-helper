from django.contrib import admin

# Register your models here.
from .models import BankAccount,LoanAccount,EntertainmentAccount,CreditAccount,UtilityAccount

admin.site.register(BankAccount)
admin.site.register(LoanAccount)
admin.site.register(EntertainmentAccount)
admin.site.register(CreditAccount)
admin.site.register(UtilityAccount)
