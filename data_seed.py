import django
import os
import random
from faker import Faker
from decimal import Decimal
from django.utils import timezone

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from store.models import Product, Customer, Order

fake = Faker()

# ---------------------------
# Create random products
# ---------------------------
categories = ["Electronics", "Books", "Clothing", "Home", "Toys"]

products = []
for _ in range(10):  # Generate 10 products
    product = Product.objects.create(
        name=fake.word().capitalize() + " " + fake.word().capitalize(),
        category=random.choice(categories),
        price=Decimal(f"{random.randint(10, 5000)}.{random.randint(0,99):02d}"),
        stock_quantity=random.randint(0, 100),
        description=fake.sentence(nb_words=10)
    )
    products.append(product)

# ---------------------------
# Create random customers
# ---------------------------
customers = []
for _ in range(10):  # Generate 10 customers
    customer = Customer.objects.create(
        name=fake.name(),
        state=fake.state_abbr(),
        city=fake.city(),
        email=fake.unique.email(),
        phone_number=fake.phone_number(),
        address=fake.address()
    )
    customers.append(customer)

# ---------------------------
# Create random orders
# ---------------------------
statuses = ['pending', 'shipped', 'delivered', 'canceled']

for _ in range(20):  # Generate 20 orders
    Order.objects.create(
        amount=random.randint(1, 5),
        customer_id=random.choice(customers),
        product_id=random.choice(products),
        order_date=timezone.now(),
        status=random.choice(statuses),
        notes=fake.sentence(nb_words=8)
    )

print("Random test data successfully inserted!")
