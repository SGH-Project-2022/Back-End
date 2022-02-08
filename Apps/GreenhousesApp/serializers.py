from .models import Greenhouse
from rest_framework import serializers
from Library.api_response import ApiResponse
from rest_framework import status
from django_countries.serializers import CountryFieldMixin


class GreenhouseSerializers(CountryFieldMixin , serializers.ModelSerializer):
    class Meta:
        model = Greenhouse
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True },  
            'user': {'write_only': True},
            'is_active':{'write_only':True},
        }
        def update(self, greenhouse ,validated_data):
            
            greenhouse.width = validated_data.get("width" , greenhouse.width)
            greenhouse.height = validated_data.get("height" , greenhouse.height)
            greenhouse.cultivation_type = validated_data.get("cultivation_type" , greenhouse.cultivation_type)
            greenhouse.water_tank_size = validated_data.get("water_tank_size" , greenhouse.water_tank_size)
            greenhouse.number_of_crops = validated_data.get("number_of_crops" , greenhouse.number_of_crops)
            greenhouse.country = validated_data.get("country" , greenhouse.country)
            
            greenhouse.save()
            

            return greenhouse
    


class ConfigureGreenhouseSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    password = serializers.CharField(max_length=10)

    def validate(self, data):
        api_response = ApiResponse()
        
        try:
            greenhouse = Greenhouse.objects.get(pk=data["id"], password=data["password"] , is_active = True)
        
        except Greenhouse.DoesNotExist:
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)
        
        else:
            
            if greenhouse.user == self.context["request"].user:
                response = api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", "This greenhouse already belongs to you.").get()
                raise serializers.ValidationError(response)
            
            elif greenhouse.user != None:
                response = api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", "This greenhosue owned by another user, please enter valid ID and password.").get()
                raise serializers.ValidationError(response)

        return data

    def save(self,  **kwargs):
        greenhouse = Greenhouse.objects.get(pk = self.data["id"], password = self.data["password"] , is_active = True)  
        greenhouse.user = self.context["request"].user
        greenhouse.save()
        return greenhouse


class GetUserGreenhouseSerializer(serializers.Serializer):    
    
    def validate(self, data):
        api_response = ApiResponse()

        if self.context["id"] is not None:
            
            try:
                Greenhouse.objects.filter( pk=self.context["id"], user=self.context["request"].user , is_active = True)
            
            except Greenhouse.DoesNotExist:
                response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This greenhouse not found").get()
                raise serializers.ValidationError(detail=response)

                    
        return data
    
    def save(self , **kwargs):
        greenhouse = Greenhouse.objects.filter(user=self.context["request"].user , is_active = True)
        return greenhouse

