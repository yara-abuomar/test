from django.db import models

class Product(models.Model):
    item=models.CharField(max_length=255)
    price=models.FloatField()
   # maxquntity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# Create your models here.
