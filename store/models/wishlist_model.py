from django.db import models
from .customer_model import Customer
from .product_model import Product

class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='WishlistItem')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.name}' de {self.customer.name}"

class WishlistItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'wishlist')

    def __str__(self):
        return f"{self.product.name} na lista '{self.wishlist.name}'"