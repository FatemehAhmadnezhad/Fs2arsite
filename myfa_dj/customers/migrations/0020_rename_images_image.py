# Generated by Django 4.1.3 on 2022-11-25 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0019_images'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
    ]
