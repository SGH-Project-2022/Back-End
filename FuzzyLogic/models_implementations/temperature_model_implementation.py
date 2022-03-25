from FuzzyLogic.models.temperature_model import TempFuzzyLogic
from rest_framework import serializers 

class TemperatureModelImplementation:
    def __init__(self) -> None:
        self.model = TempFuzzyLogic()
        self.model.fuzzification()
        self.model.apply_rules()
    
    def set_temperature_value(self, value) -> 'TemperatureModelImplementation':
        self.temperature_value = value
        return self
        
    def set_temperature_change_value(self,value) -> 'TemperatureModelImplementation':
        self.temperature_change_value = value        
        return self
    
    def process_input(self) -> 'TemperatureModelImplementation':
        self.model.set_input_values(temperature=self.temperature_value , temperature_rate=self.temperature_change_value)
        self.model.defuzzification()
        return self
    
    def get_fan_speed_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["fan_speed"]
        raise serializers.ValidationError(detail="Error on Temperature model defuzzification process")

