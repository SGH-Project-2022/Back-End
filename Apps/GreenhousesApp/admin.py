from django.contrib import admin

from Apps.GreenhousesApp.models import Greenhouse


class GreenhouseAdmin (admin.ModelAdmin):
    list_display = ('id','is_active','country','user')
    list_filter = ('created_at','country','is_active')
    
    

admin.site.register(Greenhouse , GreenhouseAdmin)
# Register your models here.
