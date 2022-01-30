from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Greenhouse(models.Model):
    width = models.CharField(max_length=4)
    height = models.CharField(max_length=4)
    
    cultivation_type = models.CharField(max_length=120)
    water_tank_size = models.CharField(max_length=10)
    number_of_crops = models.CharField(max_length=4)
    
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    
    wifi_name = models.CharField(max_length=120)
    wifi_password = models.CharField(max_length=120)
    
    image = models.CharField(max_length=150)
    

    frame_type = models.CharField(max_length=120)
    frame_price = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True) 


class GreenhouseUsers(models.Model):
    user = models.ForeignKey(User,related_name='user_id')
    greenhouse = models.ForeignKey(Greenhouse,related_name='greenhouse_id')    
    created_at = models.DateTimeField(auto_now_add=True) 
