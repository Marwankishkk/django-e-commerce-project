from itertools import product
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from home.models import Product
from cart.models import Shopping_Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def tops(request):
    products = Product.objects.all()
    top_products = Product.objects.filter(category='Tops')

    return render(request, ("categories/tops.html"), {"products": top_products})


def trousers(request):
    products = Product.objects.all()
    trousers_products = Product.objects.filter(category='Trousers')

    return render(request, ("categories/trousers.html"), {"products": trousers_products})


def add_to_cart(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    user = request.user
    try:
        cart_item = Shopping_Cart.objects.get(user=user, product=product)
        cart_item.quantity += 1
        cart_item.save()
        cart_item.update_total_price()

        messages.success(
            request, f"Added another '{product.name}' to your cart")
    except Shopping_Cart.DoesNotExist:
        cart_item = Shopping_Cart.objects.create(user=user, product=product)
        cart_item.update_total_price()
        messages.success(request, f"Added '{product.name}' to your cart")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
