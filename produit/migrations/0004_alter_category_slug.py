# Generated by Django 4.1.7 on 2023-05-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
