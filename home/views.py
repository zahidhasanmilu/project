from django.shortcuts import render
from django.http import HttpResponse
from home.models.catagory import Catagory
from home.models.products import Products


# Create your views here.
def home(request):
    products = Products.get_all_products()
    catagory = Catagory.get_all_catagories()
    catagoryId = request.GET.get('catagory')
    if catagoryId:
        products = Products.get_all_products_by_catagories(catagoryId)
    else:
        products = Products.get_all_products()
    if "user" in request.session.keys():
        return render(request, 'home/index.html', context={'item': products, 'catagories': catagory})
    return render(request, 'home/index.html', context={'item': products, 'catagories': catagory})


def trending(request):
    products = Products.get_all_products()
    catagory = Catagory.get_all_catagories()
    catagoryId = request.GET.get('catagory')

    if catagoryId:
        products = Products.get_all_products_by_catagories(catagoryId)
    else:
        products = Products.get_all_products()

    return render(request, 'home/trending.html', context={'product': products, 'catagories': catagory})


def search(request):
    # keywords = request.GET.get('keywords').split(' ')
    # results = Products.objects.filter(title__icontains=keywords[0])
    # results = results.union(Products.objects.filter(
    #     description__icontains=keywords[0]))

    # for key in keywords:
    #     results = Products.objects.filter(title__icontains=key)
    #     results = results.union(Products.objects.filter(
    #         description__icontains=key))

    if request.method == 'GET':
        keywords = request.GET.get('keywords')
        results = Products.objects.filter(title__icontains=keywords)
        return render(request, 'home/search_results.html', context={'products': results, 'invalid': True})


def details(request, pid):
    items = Products.objects.filter(pid=pid).first()

    return render(request, 'home/porduct_details.html', context={'items': items})
