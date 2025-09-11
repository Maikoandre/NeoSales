from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Order, Product, Customer
import plotly.express as px
import pandas as pd
from django.db.models import Count

def index(request):
    orders = Order.objects.order_by('-order_date')[:10]

    data = Product.objects.values('category').annotate(count=Count('id'))
    df = pd.DataFrame(list(data))
    fig = px.pie(df, names='category', values='count')
    graph_json = fig.to_json()

    total_orders = Order.objects.count()
    total_customers = Customer.objects.count()
    total_products = Product.objects.count()
    pending_orders = Order.objects.filter(status='pending').count()
    low_stock_products = Product.objects.filter(stock_quantity__lt=10).count()
    category_most_products = Product.objects.values('category') \
        .annotate(count=Count('id')) \
        .order_by('-count').first()
    top_category = category_most_products['category'] if category_most_products else 'N/A'

    context = {
        "orders": orders,
        "graph_json": graph_json
        ,"total_orders": total_orders
        ,"total_customers": total_customers
        ,"total_products": total_products
        ,"pending_orders": pending_orders
        ,"low_stock_products": low_stock_products
        ,"top_category": top_category
    }
    return render(request, "index.html", context)

def details(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'details.html', {'order': order})