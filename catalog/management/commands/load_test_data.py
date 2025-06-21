from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "deleting and then adding fixtures"

    def handle(self, *args, **options):
        self.stdout.write("Deleting old fixtures..")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Loading new ones..")
        call_command('loaddata', 'catalog/fixtures/categories.json')
        call_command('loaddata', 'catalog/fixtures/products.json')

        self.stdout.write(self.style.SUCCESS("Success!"))
