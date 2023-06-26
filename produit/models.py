from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify  #new

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True , null=True)

    class Meta:
        ordering = ['name']
        indexes = [ 
            models.Index(fields=['name']), 
            models.Index(fields=['slug']), 
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category , self).save(*args, **kwargs)


class Produit(models.Model):
    class GenereChoicesStart(models.TextChoices):
        five = "5"
        four = "4"
        three= "3"
        two  = "2"
        one  = "1" 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True , null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=900)
    start = models.CharField(max_length=13 , choices=GenereChoicesStart.choices , default=GenereChoicesStart.five)
    default_price = models.PositiveIntegerField(default=1)
    price_reduction = models.PositiveIntegerField(default=1)
    the_number_of_pieces = models.PositiveIntegerField(default=1)
    remize_day = models.DateField(default=timezone.now , verbose_name="The Offer Ends After")
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1 , verbose_name="Choice your Category") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created_at']),
            models.Index(fields=['-updated_at']),
        ]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Produit, self).save(*args, **kwargs)