from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

from django.contrib.auth.hashers import make_password, check_password

class Customer(models.Model):
    name = models.CharField(max_length=100)
    home_number = models.IntegerField()
    neighborhood = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128)  # store hashed password

    def set_password(self, raw_password):
        """Hashes and sets the password"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Checks if the raw password matches the stored hash"""
        return check_password(raw_password, self.password)


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
