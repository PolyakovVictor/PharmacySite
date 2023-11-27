from django.contrib import admin
from .models import Pharmacy, Medicine, Order


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('address',)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pharmacy',)
    list_filter = ('pharmacy',)
    search_fields = ('name', 'pharmacy__name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicine', 'pharmacy', 'delivery_address', 'phone_number', 'full_name')
    list_filter = ('pharmacy',)
    search_fields = ('medicine__name', 'pharmacy__name', 'delivery_address',)
