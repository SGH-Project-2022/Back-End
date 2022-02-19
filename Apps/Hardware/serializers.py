from rest_framework import serializers
from Apps.Greenhouses.models import Greenhouse , GreenhouseActustor , GreenhouseSensor
from .models import Sensor , Actuator , ActuatorsAction , SensorValues  
from rest_framework.response import Response
from rest_framework import status
from Library.api_response import ApiResponse
import requests
from Library.helper import project_server

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"
        

class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = "__all__"
        

class SensorValuesSerializer(serializers.Serializer):
    
    greenhouse_id = serializers.CharField()
    password = serializers.CharField()
    sensors = serializers.ListField()
    
    def validate(self, data):
        api_response = ApiResponse()

        try:
            greenhouse = Greenhouse.objects.get(pk = data["greenhouse_id"] , password = data["password"])
        except Greenhouse.DoesNotExist:
            response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "A greenhouse with this ID and password is not found.").get()
            raise serializers.ValidationError(detail=response)
        
        for sensor in data["sensors"]:
            try:
                
                sensor = Sensor.objects.get(pk = sensor['sensor_id']) 
                greenhouse_sensor = GreenhouseSensor.objects.get(sensor = sensor , greenhouse = greenhouse)
                print(greenhouse_sensor)
                return Response(greenhouse_sensor)
                # print(mySensor.name)
                # print(mySensor[0].id)
                # greenhouse = Greenhouse.sensors.through.get_deferred_fields(greenhouse_id = data("greenhouse_id") , sensor_id = mySensor.id)
                # greenhouse = Greenhouse.objects.get(pk = data("greenhouse_id") , password = data["password"] , sensors = mySensor.id)
            except Greenhouse.DoesNotExist:
                response = api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("errors", "This sensor not integrated with this greenhouse").get()
                raise serializers.ValidationError(detail=response)
            
            
        return data
        

class ActuatorActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActuatorsAction
        fields = "__all__"
        
    