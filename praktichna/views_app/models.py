from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=100)  # Назва предмета
    description = models.TextField(blank=True)  # Опис
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Ціна
    is_tradable = models.BooleanField(default=True)  # Чи можна обмінювати
    added_at = models.DateTimeField(default=timezone.now)  # Дата додавання
    rarity = models.CharField(
        max_length=20,
        choices=[
            ('common', 'Звичайний'),
            ('rare', 'Рідкісний'),
            ('unique', 'Унікальний'),
            ('unusual', 'Незвичайний'),
        ],
        default='unique'
    )
    quantity = models.IntegerField(default=0)  # Кількість
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категорія

    def __str__(self):
        return f"{self.name} ({self.category.name})"
