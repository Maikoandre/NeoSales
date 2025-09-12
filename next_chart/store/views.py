from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from .models import Order, Product, Customer
import json
from .forms import CustomerForm, ProductForm, OrderForm

def index(request):
    orders = Order.objects.order_by('-order_date')
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
        
    return render(request, 'forms/customers.html', {'form': form})

def register_products(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                price=form.cleaned_data['price'],
                stock_quantity=form.cleaned_data['stock_quantity']
            )
            return redirect('register_products')
    else:
        form = ProductForm()
        
    return render(request, 'forms/products.html', {'form': form})

def register_orders(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                amount=form.cleaned_data['amount'],
                customer_id=form.cleaned_data['customer_id'],
                product_id=form.cleaned_data['product_id'],
                status=form.cleaned_data['status'],
                notes=form.cleaned_data.get('notes', '')
            )
            return redirect('register_orders')
    else:
        form = OrderForm()
        
    return render(request, 'forms/orders.html', {'form': form})

def manage_customers(request):
    customers = Customer.objects.all()
    return render(request, 'management/manage_customers.html', {'customers': customers})

def update_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('manage_customers')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'management/update_customer.html', {'form': form})

def delete_customer(request, id):
    if request.method == "POST":
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
    return redirect('manage_customers')