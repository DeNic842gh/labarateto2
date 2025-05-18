from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Show category name and description in the table


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rarity', 'is_tradable', 'quantity', 'category')  # Customize admin list view
    list_filter = ('rarity', 'is_tradable', 'category')  # Add rarity and tradability filters
    search_fields = ('name', 'description')  # Search for items by name/description
