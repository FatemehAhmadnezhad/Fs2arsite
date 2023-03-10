# Generated by Django 4.1.2 on 2022-11-09 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='userName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(choices=[('POSTER', 'پوستر'), ('BANNER', 'بنر'), ('BUSINESSCARD', 'بیزینس کارت')], max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('contentn', models.TextField()),
                ('description', models.TextField()),
                ('imge', models.ImageField(upload_to='')),
                ('Customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
