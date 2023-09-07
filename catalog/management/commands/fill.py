from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        categories_list = [
            {"title": "Category A", "description": "Category A description"},
            {"title": "Category B", "description": "Category B description"},
        ]

        categories_for_create = []
        for category_item in categories_list:
            categories_for_create.append(Category(**category_item))

        Category.objects.bulk_create(categories_for_create)
