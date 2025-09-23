from django.db import models
from .product_model import Product
from .customer_model import Customer

class Order(models.Model):
    amount = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('canceled', 'Canceled')],
        default='pending'
    )
    notes = models.TextField(blank=True, null=True)