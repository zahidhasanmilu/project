from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from cart.models import cartItem
from home.models import Products

# Create your views here.


@login_required
def cart(request, uid):
    cart_item = cartItem.objects.filter(uid=uid, in_cart=True)
    cart_items = []
    cart_total = 0.0
    for item in cart_item:
        product = Products.objects.filter(pid=item.pid).first()

        p = {'pid': product.pid,
             'title': product.title,
             'image': product.image,
             'qty': item.qty,
             'price': float(product.price)*float(item.qty)
             }
        cart_items.append(p)
        cart_total = cart_total + p['price']
    return render(request, 'cart/cart.html', context={'cart_items': cart_items, 'cart_total': cart_total})


@login_required
def addTocart(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        uid = request.POST['uid']
        qty = request.POST['qty']
        cart_item = cartItem(
            pid=pid,
            uid=uid,
            qty=qty,
        )
        cart_item.save()
        return redirect('/')
    return render(request, 'cart/cart.html')
