from django.contrib.auth.backends import BaseBackend
from .models import Customer

class CustomerAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            customer = Customer.objects.get(email=username)
            if customer.check_password(password):
                return customer
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None