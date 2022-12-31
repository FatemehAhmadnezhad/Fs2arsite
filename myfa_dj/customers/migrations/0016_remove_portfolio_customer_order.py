# Generated by Django 4.1.3 on 2022-11-19 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0015_remove_portfolio_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='customer',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('case', models.CharField(choices=[('POSTER', 'پوستر'), ('BANNER', 'بنر'), ('BUSINESSCARD', 'بیزینس کارت')], max_length=50)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]