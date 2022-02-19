from django.db import models
from django_countries.fields import CountryField
from django.utils.crypto import get_random_string
from Apps.Users.models import User
from Apps.Plants.models import Plant
from Apps.Hardware.models import Sensor
from Apps.Hardware.models import Actuator
# Create your models here.


class Greenhouse(models.Model):

    width = models.FloatField()
    height = models.FloatField()

    password = models.CharField(max_length=10, default=get_random_string(length=7))

    cultivation_type = models.CharField(max_length=120)
    water_tank_size = models.FloatField()
    number_of_crops = models.IntegerField()

    # city = models.CharField(max_length=120)
    country = CountryField()

    # wifi_name = models.CharField(max_length=120)
    # wifi_password = models.CharField(max_length=120)

    is_active = models.BooleanField(default=True)

    image = models.ImageField(upload_to="GreenhouseUploads/")

    user = models.ForeignKey(User, related_name='user_id',blank=True, null=True, on_delete=models.CASCADE)

    frame_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    
    plants = models.ManyToManyField(Plant , related_name="greenhouse_plants"  ,through= 'GreenhousePlant')
    
    sensors = models.ManyToManyField(Sensor ,  related_name="greenhouse_sensors" , through= 'GreenhouseSensor')
    actuators = models.ManyToManyField(Actuator , related_name="greenhouse_actuators" , through= 'GreenhouseActustor')
    
    
    def __str__(self):
        return str(self.id)



class GreenhousePlant(models.Model):
    plant = models.ForeignKey(Plant , on_delete=models.CASCADE)
    greenhouse = models.ForeignKey(Greenhouse , on_delete=models.CASCADE)
    number_of_crops = models.IntegerField( null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    
class GreenhouseSensor(models.Model):
    greenhouse = models.ForeignKey(Greenhouse , on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor , on_delete=models.CASCADE)
    position = models.CharField(max_length=200 , null=True , blank=True)    

class GreenhouseActustor(models.Model):
    greenhouse = models.ForeignKey(Greenhouse , on_delete=models.CASCADE)
    actuator = models.ForeignKey(Actuator , on_delete=models.CASCADE)
    position = models.CharField(max_length=200 , null=True , blank=True)
    