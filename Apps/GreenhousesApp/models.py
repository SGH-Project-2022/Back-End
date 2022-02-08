from django.db import models
from django_countries.fields import CountryField
from django.utils.crypto import get_random_string
from Apps.UsersApp.models import User
from Apps.PlantsApp.models import Plant
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
    
    
    plants = models.ManyToManyField(Plant , related_name="greenhouse_plant" )
    
    def __str__(self):
        return str(self.id)
