# Generated by Django 4.1.7 on 2023-05-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0006_category_produit_cat_slug_eef8b4_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
