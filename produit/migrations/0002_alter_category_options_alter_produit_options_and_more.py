from django.db import migrations , models

class Migration(migrations.Migration):
    dependencies = [
        ('produit', '0001_initial'),
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='slug',
            field=models.SlugField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='produit_cat_name_796e38_idx'),
        ),
        migrations.AddIndex(
            model_name='produit',
            index=models.Index(fields=['id', 'slug'], name='produit_pro_id_c773b1_idx'),
        ),
        migrations.AddIndex(
            model_name='produit',
            index=models.Index(fields=['title'], name='produit_pro_title_f39cca_idx'),
        ),
        migrations.AddIndex(
            model_name='produit',
            index=models.Index(fields=['-created_at'], name='produit_pro_created_539913_idx'),
        ),
        migrations.AddIndex(
            model_name='produit',
            index=models.Index(fields=['-updated_at'], name='produit_pro_updated_0bd9b2_idx'),
        ),
    ]
