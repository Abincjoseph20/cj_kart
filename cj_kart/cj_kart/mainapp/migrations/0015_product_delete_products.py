# Generated by Django 5.0.7 on 2024-08-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_remove_cart_items_cart_remove_cart_items_product_and_more'),
        ('mainapp', '0014_rename_prodapp_products_crated_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('CR', 'Crud'), ('MK', 'Milk'), ('LS', 'Lassi'), ('MS', 'MilkShake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IH', 'Ice-cream')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
                ('product_quantity', models.FloatField()),
                ('modified_date', models.DateField(auto_now=True)),
                ('crated_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
