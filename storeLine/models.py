from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='store_profile/', verbose_name="Image for your store")
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name