from django.db import models
from Apps.GreenhouseApp.models import Greenhouse

class Plants(models.Model):
    type =  models.CharField(max_length=120)
    image = models.CharField(max_length=150)
    
class GreenhousePlants(models.Model):
    greenhouse = models.ForeignKey(Greenhouse , related_name="greenhosue_id")
    created_at = models.DateTimeField(auto_now_add=True) 
