from django.core.management.base import BaseCommand
from views_app.models import Category, Item


class Command(BaseCommand):
    help = "Seeds the database with initial data"

    def handle(self, *args, **kwargs):
        # Create categories
        electronics = Category.objects.create(name="Electronics", description="Electronic gadgets and devices")
        books = Category.objects.create(name="Books", description="Various genres of books")
        fashion = Category.objects.create(name="Fashion", description="Clothing and accessories")

        # Add items
        Item.objects.create(name="Smartphone", description="Latest model", price=699.99, is_tradable=True,
                            rarity='unique', quantity=5, category=electronics)
        Item.objects.create(name="Laptop", description="Gaming laptop", price=1200.50, is_tradable=False,
                            rarity='rare', quantity=2, category=electronics)
        Item.objects.create(name="Wireless Earbuds", description="Noise-canceling capability", price=199.99,
                            is_tradable=True, rarity='unusual', quantity=10, category=electronics)
        Item.objects.create(name="Fiction Book", description="Bestselling novel", price=9.99, is_tradable=True,
                            rarity='common', quantity=30, category=books)
        Item.objects.create(name="Cookbook", description="Recipes from around the world", price=14.99,
                            is_tradable=True, rarity='common', quantity=20, category=books)
        Item.objects.create(name="Winter Jacket", description="Insulated for cold temperatures", price=79.99,
                            is_tradable=True, rarity='unique', quantity=3, category=fashion)
        Item.objects.create(name="Sunglasses", description="Polarized lenses", price=29.99, is_tradable=True,
                            rarity='rare', quantity=15, category=fashion)
        Item.objects.create(name="Designer Handbag", description="Luxury brand", price=249.99, is_tradable=False,
                            rarity='unique', quantity=1, category=fashion)
        Item.objects.create(name="Tablet", description="10-inch screen", price=299.99, is_tradable=True,
                            rarity='rare', quantity=7, category=electronics)
        Item.objects.create(name="Mystery Book", description="Enthralling mystery novel", price=12.99,
                            is_tradable=True, rarity='common', quantity=25, category=books)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database with initial data!"))
