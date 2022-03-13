from django.contrib import admin
from .models.products import Products
from .models.catagory import Catagory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pid', 'title', 'price', 'catagory',
                    'description', 'image', 'delivery', 'stock']


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Products, ProductAdmin)
admin.site.register(Catagory, CatagoryAdmin)
