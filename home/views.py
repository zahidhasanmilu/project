from django.shortcuts import render
from django.http import HttpResponse
from home.models.catagory import Catagory
from home.models.product import Product


# Create your views here.
def home(request):
    products = Product.get_all_products()
    catagory = Catagory.get_all_catagories()    
    catagoryId = request.GET.get('catagory')
    
    if catagoryId :
        products = Product.get_all_products_by_catagories(catagoryId)
    else:
        products = Product.get_all_products()
    
    return render(request,'home/index.html', context={'item':products, 'catagories':catagory})


def signup(request):
    return render(request, 'home/signup.html')