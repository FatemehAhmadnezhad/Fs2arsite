# Generated by Django 4.1.3 on 2022-12-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0026_rename_created_by_portfolio_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='o_image',
            field=models.ImageField(blank=True, null=True, upload_to='o/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='p_image',
            field=models.ImageField(blank=True, null=True, upload_to='p/'),
        ),
    ]
