from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['oid', 'uid', 'full_name',
                    'email', 'qty', 'pid', 'price', 'address',
                    'town', 'zip_code', 'phone', 'comment']


admin.site.register(Order, OrderAdmin)
