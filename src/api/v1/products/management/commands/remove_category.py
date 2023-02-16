from api.v1.products.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate random Category"

    def handle(self, *args, **kwargs):

        for i in range(1, 5000):
            name = f'category{i}'
            category = Category.objects.get(name=name)
            category.delete()
                
