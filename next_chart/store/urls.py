from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forms/customers/", views.customers, name="customers"),
    path("details/<int:order_id>/", views.details, name="details"),
]
