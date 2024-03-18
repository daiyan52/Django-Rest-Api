from django.db import models

# Create your models here.
class Actor(models.Model):
    fname = models.CharField(max_length=16)
    lname = models.CharField(max_length=16)
    age = models.IntegerField()
    
    def __str__(self):
        return self.fname

class Movie(models.Model):
        hits_movie = models.CharField(max_length=32)
        actor = models.ForeignKey(Actor,on_delete=models.CASCADE, related_name='lead_actor')
        realsed_date = models.DateField()
        box_office_collection = models.FloatField()
        
        def __str__(self):
            return self.hits_movie