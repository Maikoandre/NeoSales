# store/management/commands/populate_db.py

import random
from django.core.management.base import BaseCommand
from faker import Faker

# Imports ajustados para a sua estrutura de models
from store.models.customer_model import Customer
from store.models.product_model import Product
from store.models.order_model import Order
from store.models.wishlist_model import Wishlist, WishlistItem

class Command(BaseCommand):
    help = 'Populates the database with a specified number of fake entries for each model.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            help='The number of items to create for each model',
            default=50
        )

    def handle(self, *args, **options):
        number_of_items = options['number']
        faker = Faker('pt_BR')

        self.stdout.write(self.style.SUCCESS(f'Iniciando o povoamento do banco de dados com {number_of_items} itens...'))

        # --- Limpando dados antigos ---
        self.stdout.write('Limpando dados antigos...')
        WishlistItem.objects.all().delete()
        Order.objects.all().delete()
        Wishlist.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()

        # --- Criando Produtos ---
        self.stdout.write('Criando produtos...')
        products = []
        categories = ['Eletrônicos', 'Roupas', 'Livros', 'Casa', 'Esportes']
        for _ in range(number_of_items):
            product = Product(
                name=faker.word().capitalize() + ' ' + faker.word().capitalize(),
                category=random.choice(categories),
                price=round(random.uniform(19.99, 999.99), 2),
                stock_quantity=random.randint(0, 200),
                description=faker.paragraph(nb_sentences=3)
            )
            products.append(product)
        Product.objects.bulk_create(products)
        all_products = list(Product.objects.all())

        # --- Criando Clientes ---
        self.stdout.write('Criando clientes...')
        customers = []
        for _ in range(number_of_items):
            customer = Customer(
                name=faker.name(),
                home_number=faker.building_number(),
                neighborhood=faker.bairro(),
                state=faker.state_abbr(),
                city=faker.city(),
                email=faker.unique.email(),
                phone_number=faker.phone_number()
            )
            customer.set_password('12345') 
            customer.save()
            customers.append(customer)
        all_customers = list(Customer.objects.all())

        # --- Criando Pedidos ---
        self.stdout.write('Criando pedidos...')
        orders = []
        order_statuses = ['pending', 'shipped', 'delivered', 'canceled']
        for _ in range(number_of_items * 2):
            customer = random.choice(all_customers)
            product = random.choice(all_products)
            order = Order(
                customer_id=customer, # Corrigido de customer_id para customer
                product_id=product,   # Corrigido de product_id para product
                amount=random.randint(1, 5),
                status=random.choice(order_statuses),
                notes=faker.sentence() if random.choice([True, False]) else ''
            )
            orders.append(order)
        Order.objects.bulk_create(orders)

        # --- Criando Wishlists e Itens da Wishlist ---
        self.stdout.write('Criando wishlists e seus itens...')
        wishlist_items = []
        for customer in all_customers:
            for i in range(random.randint(1, 2)):
                wishlist = Wishlist.objects.create(
                    name=f'Favoritos de {customer.name.split()[0]} #{i+1}',
                    customer=customer
                )
                products_for_wishlist = random.sample(all_products, k=random.randint(2, 7))
                for product in products_for_wishlist:
                    item = WishlistItem(
                        wishlist=wishlist,
                        product=product
                    )
                    wishlist_items.append(item)
        WishlistItem.objects.bulk_create(wishlist_items)

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso! ✅'))