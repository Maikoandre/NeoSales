from django.db import models
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
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        """Hashes and sets the password"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Checks if the raw password matches the stored hash"""
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.name