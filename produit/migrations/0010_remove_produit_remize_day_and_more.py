# Generated by Django 4.1.7 on 2023-08-21 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0009_rename_product_like_produit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='remize_day',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='the_number_of_pieces',
        ),
    ]
