from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def cart(request):
    return HttpResponse("Cart")