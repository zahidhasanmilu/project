from django.contrib import admin
from .models.product import Product
from .models.catagory import Catagory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'catagory',
                    'description', 'image', 'delivery', 'stock', 'quantiles']


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Catagory, CatagoryAdmin)
