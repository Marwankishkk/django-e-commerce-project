from django.urls import path, include
from . import views

urlpatterns = [
    path("tops", views.tops, name="tops"),
    path("trousers", views.trousers, name="trousers"),

    path('add-to-cart/<int:product_id>/',
         views.add_to_cart, name='add_to_cart'),
]
