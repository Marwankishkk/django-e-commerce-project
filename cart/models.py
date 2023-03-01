from django.db import models
from django.contrib.auth.models import User
from home.models import Product
from collections import defaultdict


class Shopping_Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    def update_total_price(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price

        super().save(*args, **kwargs)
