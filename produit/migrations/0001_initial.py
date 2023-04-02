# Generated by Django 4.1.7 on 2023-04-01 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='produit/')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=900)),
                ('start', models.CharField(choices=[('5', 'Five'), ('4', 'Four'), ('3', 'Three'), ('2', 'Two'), ('1', 'One')], default='5', max_length=13)),
                ('default_price', models.PositiveIntegerField(default=1)),
                ('price_reduction', models.PositiveIntegerField(default=1)),
                ('the_number_of_pieces', models.PositiveIntegerField(default=1)),
                ('remize_day', models.DateField(default=django.utils.timezone.now, verbose_name='The Offer Ends After')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produit.category', verbose_name='Choice your Category')),
            ],
        ),
    ]
