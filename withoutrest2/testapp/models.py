from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField
    ename = models.CharField(max_length=25)
    esal = models.FloatField()
    eaddress = models.CharField(max_length=100)    