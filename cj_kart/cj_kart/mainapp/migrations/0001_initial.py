# Generated by Django 5.0.7 on 2024-07-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('CR', 'Crud'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'MilkShake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-cream')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
