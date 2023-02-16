from api.v1.products.models import Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Generate random Category"

    def handle(self, *args, **kwargs):

        list((Category.objects.create(creator_id=1, name=f'category{i}')) for i in range(1, 500))


        # for i in range(1, 10000):
            
        #     Category.objects.create(
        #         creator_id=1,
        #         name=f'categor{i}',
        #     )
