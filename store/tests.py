from django.test import TestCase, Client
from django.urls import reverse
import models
import json

class StoreTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = models.Customer.objects.create(name="John Doe", email="john.doe@email.com")
        self.product = models.Product.objects.create(name="Laptop", price=999.99, stock_quantity=45)
        self.order = models.Order.objects.create(customer=self.customer, product=self.product, date="2023-10-01", status="pending")

    def test_register_customers_view_get(self):
        url = reverse('register_customers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms/customers.html')