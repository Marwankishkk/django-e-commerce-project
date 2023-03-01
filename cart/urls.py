from django.urls import path, include
from . import views

urlpatterns = [
    path("cart", views.cart, name="cart"),
    path('remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
]
