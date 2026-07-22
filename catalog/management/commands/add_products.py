from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command('loaddata', 'catalog_fixture.json')

        # category_phone = Category.objects.get(name='Телефоны')
        # category_tele = Category.objects.get(name='Телевизоры')
        #
        # products = [
        #     {'name': 'Samsung Galaxy 1', 'description': 'Самый первый телефон',
        #      'category': category_phone, 'price':'4000'},
        #     {'name': 'Samsung Galaxy 2', 'description': 'Самый второй телефон',
        #      'category': category_phone, 'price': '5000'},
        #     {'name': 'Samsung Galaxy 3', 'description': 'Самый третий телефон',
        #      'category': category_phone, 'price': '6000'},
        #     {'name': 'LG 1', 'description': 'Самый первый телевизор',
        #      'category': category_tele, 'price': '14000'},
        #     {'name': 'LG 2', 'description': 'Самый второй телевизор',
        #      'category': category_tele, 'price': '15000'},
        #     {'name': 'LG 3', 'description': 'Самый третий телевизор',
        #      'category': category_tele, 'price': '16000'},
        #     {'name': 'LG 44', 'description': 'Самый новый телевизор',
        #      'category': category_tele, 'price': '100000'},
        # ]
        #
        #
        #
        # for product_data in products:
        #     product, created = Product.objects.get_or_create(**product_data)
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Successfully added book: {product.name}'))
        #     else:
        #         self.stdout.write(self.style.WARNING(f'Book already exists: {product.name}'))