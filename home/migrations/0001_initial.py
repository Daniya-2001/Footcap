# Generated by Django 4.1.7 on 2023-04-30 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.models.get_file_path)),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default,1=Trending')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=home.models.get_file_path)),
                ('description', models.CharField(max_length=500)),
                ('quntity', models.IntegerField()),
                ('orginal_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default,1=Trending')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_qty', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
