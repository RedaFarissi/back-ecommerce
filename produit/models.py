from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

class Produit(models.Model):
    class GenereChoicesStart(models.TextChoices):
        five = "5"
        four = "4"
        three= "3"
        two  = "2"
        one  = "1" 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produit/')
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
    def __str__(self):
        return self.title