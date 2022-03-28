from django.contrib import admin
from .models import cartItem


class cartItemAdmin(admin.ModelAdmin):
    list_display = ['cid', 'uid', 'pid', 'qty',
                    'in_cart']


admin.site.register(cartItem, cartItemAdmin)
