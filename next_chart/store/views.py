from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from .models import Order, Product, Customer
import json
from .forms import CustomerForm

def index(request):
    # Get the 10 most recent orders
    orders = Order.objects.order_by('-order_date')[:10]
    # Prepare data for the pie chart
    category_data= (
        Product.objects.values('category') \
        .annotate(count=Count('id')) \
        .order_by('-category')
    )
    labels =[item['category'] for item in category_data]
    data = [item['count'] for item in category_data]
    chart_data = {
        "labels": labels,
        "datasets": [{
            "label": "Products per Category",
            "data": data,
            "backgroundColor": [
                "#4e79a7", "#f28e2b", "#e15759",
                "#76b7b2", "#59a14f", "#edc949",
                "#af7aa1", "#ff9da7", "#9c755f", "#bab0ab"
            ][:len(labels)],
        }]
    }

    # Summary statistics
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
        "chart_data": json.dumps(chart_data)
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

def register_customers(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_customers')
    else:
        form = CustomerForm()
        
    return render(request, 'customers.html', {'form': form})