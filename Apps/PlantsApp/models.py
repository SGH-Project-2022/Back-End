from django.db import models

class Plant(models.Model):
    type =  models.CharField(max_length=120)
    image = models.ImageField(upload_to="PlantsUploads/")
    is_supported = models.BooleanField(default=False)

    def __str__(self):
        return self.type
    
# class GreenhousePlants(models.Model):
#     voucher_code = models.ManyToOneRel(field = "voucher_code", field_name = "voucher_code", to = "code")(1)

#     greenhouse = models.ForeignKey(Greenhouse , related_name="greenhosue_id")
#     created_at = models.DateTimeField(auto_now_add=True) 
