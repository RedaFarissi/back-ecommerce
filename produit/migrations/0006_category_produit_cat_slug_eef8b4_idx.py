# Generated by Django 4.1.7 on 2023-05-02 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0005_alter_produit_slug'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['slug'], name='produit_cat_slug_eef8b4_idx'),
        ),
    ]