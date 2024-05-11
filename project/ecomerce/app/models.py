from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=150)
    quantity = models.IntegerField(default=1)
    price=models.IntegerField(max_length=150)