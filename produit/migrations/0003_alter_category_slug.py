# Generated by Django 4.1.7 on 2023-05-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_alter_category_options_alter_produit_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
