from FuzzyLogic.models.ph_model import PHFuzzyLogic
from rest_framework import serializers 

class PHModelImplementation:
    def __init__(self) -> None:
        self.model = PHFuzzyLogic()
        self.model.fuzzification()
        self.model.apply_rules()
        
    def set_ph_value(self, value) -> 'PHModelImplementation':
        self.ph_value = value
        return self
        
    def set_water_level_value(self,value) -> 'PHModelImplementation':
        self.water_level_value = value        
        return self
    
    def process_input(self) -> 'PHModelImplementation':
        self.model.set_input_values(ph_value = self.ph_value, water_level_value= self.water_level_value)
        self.model.defuzzification()
        return self
    
    def get_ph_pump_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["ph_pump"]
        raise serializers.ValidationError(detail="Error on PH model defuzzification process")
    
    def get_alkaline_pump_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["alkaline_pump"]
        raise serializers.ValidationError(detail="Error on PH model defuzzification process")
    