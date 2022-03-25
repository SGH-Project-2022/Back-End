from .models_implementations.ph_model_implementation import PHModelImplementation
from .models_implementations.temperature_model_implementation import TemperatureModelImplementation
from Library.helper import ModelObjectsHelper
from .automated_action import request
from Apps.Hardware.hardware_library.sensors import TempratureSensor,  PHSensor , WaterLevelSensor
from Apps.Hardware.hardware_library.actuators import FanActuator , AlkalinePumpActuator , PHPumpActuator


temp_model = TemperatureModelImplementation()
ph_model = PHModelImplementation()

temperature_change_rate = 10

class FuzzyImplementation:
    
    def set_sensors_values(self, sensors_values:list):
        self.modelObjects = ModelObjectsHelper()
        self.modelObjects.set_objects(sensors_values)
        return self
    def __implemet_temp(self):
        object = self.modelObjects.get_object(1)
        print(object)
        temp_model.set_temperature_value(object.value).set_temperature_change_value(temperature_change_rate).process_input()
        return temp_model.get_fan_speed_value()
    
    def __implemet_ph(self):
        ph_object = self.modelObjects.get_object(PHSensor.ID)
        water_object = self.modelObjects.get_object(WaterLevelSensor.ID)
        print(f"water_object {water_object}")
        ph_model.set_ph_value(ph_object.value).set_water_level_value(water_object.value).process_input()
        return [ph_model.get_ph_pump_value() , ph_model.get_alkaline_pump_value()]

    def take_actions(self):
        temp = self.__implemet_temp()
        print(temp)
        print(f"Fann Speed From Fuzzy --> {temp}")
        request(1,"mqN9weY",FanActuator.ID,temp)
        
        ph = self.__implemet_ph()
        print(f"PH Pump From Fuzzy --> {ph[0]}")
        print(f"Alkaline Pump  From Fuzzy --> {ph[1]}")
        request(1,"mqN9weY",PHPumpActuator.ID, 1 ,ph[0])
        request(1,"mqN9weY",AlkalinePumpActuator.ID , 1 ,ph[1])
        