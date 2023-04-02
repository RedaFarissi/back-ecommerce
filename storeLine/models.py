from django.db import models
from datetime import date

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name