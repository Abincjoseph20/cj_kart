# Generated by Django 5.0.7 on 2024-08-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_alter_products_category_alter_products_prodapp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prodapp',
            new_name='crated_date',
        ),
        migrations.RemoveField(
            model_name='products',
            name='composition',
        ),
        migrations.AddField(
            model_name='products',
            name='modified_date',
            field=models.DateField(auto_now=True),
        ),
    ]
