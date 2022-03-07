from django.shortcuts import render
from django.http import HttpResponse

from home.models.product import Product


# Create your views here.
def home(request):
    items = Product.get_all_products()
    
    
    return render(request,'home/index.html', context={'item':items})