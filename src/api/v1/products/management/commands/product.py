from api.v1.products.models import Product, Category
from api.v1.products.enums import ValueType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate random Category"
    def handle(self, *args, **kwargs):
        number = Category.objects.get(name='category1')

        list((Product.objects.create(
            category_id=number.id,
            author_id=1,
            title=f'product{i}',
            value_type=ValueType.p.name,
            region='Toshkent',
            district='Olmazor',
        )) for i in range(1, 5000))