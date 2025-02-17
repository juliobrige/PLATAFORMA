
from django.contrib import admin
from .models import MpesaPayment

@admin.register(MpesaPayment)
class MpesaPaymentAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'amount', 'transaction_id', 'transaction_date', 'status')
    search_fields = ('phone_number', 'transaction_id')
    list_filter = ('status', 'transaction_date')