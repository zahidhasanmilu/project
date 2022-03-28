from itertools import product
from math import prod
from django.shortcuts import redirect, render
from django.views import View
from home.models import Products
from cart.models import cartItem
from checkout.models import Order
# from django.contrib.auth.decorators import login_required


def checkout(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        address = request.POST['address']
        town = request.POST['town']
        phone = request.POST['phone']
        email = request.POST['email']
        zip_code = request.POST['zip_code']
        comment = request.POST['comment']
        uid = request.POST['uid']
        cart_item = cartItem.objects.filter(uid=uid, in_cart=True)
        for item in cart_item:
            product = Products.objects.get(pid=item.pid)
            price = float(product.price)*float(item.qty)
            orders = Order(
                full_name=full_name,
                address=address,
                town=town,
                phone=phone,
                email=email,
                zip_code=zip_code,
                comment=comment,
                uid=uid,
                pid=item.pid,
                price=price,
                qty=item.qty
            )
            orders.save()
            item.in_cart = False
            item.save()
        return redirect('/')
    return render(request, 'checkout/checkout.html')
