# Generated by Django 4.1.3 on 2022-12-14 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0028_alter_order_title_alter_portfolio_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='title',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='title',
        ),
    ]