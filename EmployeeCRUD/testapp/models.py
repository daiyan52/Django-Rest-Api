from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=32)
    salary = models.FloatField()
    address = models.CharField(max_length=64)