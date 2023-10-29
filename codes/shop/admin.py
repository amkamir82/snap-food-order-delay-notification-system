from django.contrib import admin

from shop.models import Vendor, Order


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'delivery_duration',
        'delivery_time',
    )
    