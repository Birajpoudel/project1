# Generated by Django 4.0.2 on 2022-03-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
