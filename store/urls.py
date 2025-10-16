from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Customer
    path("forms/customers/", views.register_customers, name="register_customers"),
    path("management/customers/", views.manage_customers, name="manage_customers"),
    path('management/customers/<int:id>/delete/', views.delete_customer, name='delete_customer'),
    path("management/customers/<int:id>/edit/", views.update_customer, name="update_customer"),
    # Product
    path("forms/products/", views.register_products, name="register_products"),
    path("management/products/", views.manage_products, name="manage_products"),
    path("management/products/<int:id>/edit/", views.update_product, name="update_product"),
    path('management/products/<int:id>/delete/', views.delete_product, name='delete_product'),
    # Order
    path("forms/orders/", views.register_orders, name="register_orders"),
    path("management/orders/", views.manage_orders, name="manage_orders"),
    path("management/orders/<int:id>/edit/", views.update_order, name="update_order"),
    path('management/orders/<int:id>/delete/', views.delete_order, name='delete_order'),
    path("details/<int:order_id>/", views.details, name="details"),
    # Authentication
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
