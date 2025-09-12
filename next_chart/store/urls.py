from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forms/customers/", views.register_customers, name="register_customers"),
    path("forms/products/", views.register_products, name="register_products"),
    path("forms/orders/", views.register_orders, name="register_orders"),
    path("management/customers/", views.manage_customers, name="manage_customers"),
    path("management/customers/<int:id>/edit/", views.update_customer, name="update_customer"),
    path('management/customers/<int:id>/delete/', views.delete_customer, name='delete_customer'),
    path("details/<int:order_id>/", views.details, name="details"),
]
