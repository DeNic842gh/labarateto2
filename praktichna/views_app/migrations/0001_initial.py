# Generated by Django 5.2 on 2025-05-18 21:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_tradable', models.BooleanField(default=True)),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('rarity', models.CharField(choices=[('common', 'Звичайний'), ('rare', 'Рідкісний'), ('unique', 'Унікальний'), ('unusual', 'Незвичайний')], default='unique', max_length=20)),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='views_app.category')),
            ],
        ),
    ]
