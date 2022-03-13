from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def cart(request, uid):

    return render(request, 'cart/cart.html')
