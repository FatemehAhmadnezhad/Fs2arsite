# Generated by Django 4.1.3 on 2022-11-27 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0020_rename_images_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
