from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Order

def index(request):
    orders = Order.objects.all()
    return render(request, "index.html", {"orders": orders})

def details(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'details.html', {'order': order})
