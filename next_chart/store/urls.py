from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forms/customers/", views.register_customers, name="register_customers"),
    path("forms/products/", views.register_products, name="register_products"),
    path("details/<int:order_id>/", views.details, name="details"),
]
