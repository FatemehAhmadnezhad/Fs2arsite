# Generated by Django 4.1.3 on 2022-11-25 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0017_order_image_portfolio_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='image',
        ),
    ]