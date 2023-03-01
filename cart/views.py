from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shopping_Cart
from home.models import Product
# Create your views here.
from .models import Shopping_Cart
from django.views.decorators.http import require_POST


def cart(request):
    cart_items = Shopping_Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    context = {'cart_items': cart_items, 'total_price': total_price}

    return render(request, 'cart/cart.html', context)


@require_POST
@login_required
def remove_from_cart(request):
    product_id = request.POST.get('product_id')

    try:
        cart_item = Shopping_Cart.objects.get(
            user=request.user, product_id=product_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            cart_item.delete()
        cart_item.update_total_price()
        cart_items = Shopping_Cart.objects.filter(user=request.user)
        total_price = sum(item.total_price for item in cart_items)
    except Shopping_Cart.DoesNotExist:
        cart_items = []
        total_price = 0

    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'cart/cart.html', context)
