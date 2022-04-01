from Apps.Hardware.models import Actuator, ActuatorsAction
from FuzzyLogic.models.ph_model import PHFuzzyLogic
from rest_framework import serializers 
from Apps.Greenhouses.greenhouse_data_model import GreenhouseDataModel
from Apps.Hardware.sensors import PHSensor , WaterLevelSensor
from Apps.Hardware.actuators import PHPumpActuator , AlkalinePumpActuator
# from Apps.Hardware.serializers.requests_serializers import TakeAutomatedActionSerializer
from datetime import datetime
from FuzzyLogic.fuzzy_logic_system_settings import TIME_BETWEEN_FUZZY_ACTIONS

class PHModelImplementation:
    
    def __check_date(self, action_date):
        difference  = datetime.now() - datetime.strptime(str(action_date)[:19] , '%Y-%m-%d %H:%M:%S')
        
        if  difference < TIME_BETWEEN_FUZZY_ACTIONS:
            return False
        return True      
    
    def validation(self):
        greenhouse = self.__greenhouse_data.get_greenhouse()
        ph_pump = Actuator.objects.get(pk = PHPumpActuator.ID)
        last_ph_pump_action = ActuatorsAction.get_last_automated_actions(greenhouse, ph_pump)
        
        alkaline_pump = Actuator.objects.get(pk = AlkalinePumpActuator.ID)
        last_alkaline_pump_action = ActuatorsAction.get_last_automated_actions(greenhouse, alkaline_pump)

        if not self.__check_date(last_alkaline_pump_action.created_at):
            return False
        
        if not self.__check_date(last_ph_pump_action.created_at):
            return False
        
        return True
    
    def set_greenhouse_data_model(self , greenhouse_data :GreenhouseDataModel)->'PHModelImplementation':
        self.__greenhouse_data = greenhouse_data
        return self
    
    def get_greenhouse_data_model(self )->GreenhouseDataModel:
        return  self.__greenhouse_data
    
    def make_actions(self) -> 'PHModelImplementation':
        
        self.model = PHFuzzyLogic()
        self.model.fuzzification()
        self.model.apply_rules()
        
        ph_value = self.__greenhouse_data.get_sensor_object(PHSensor.ID).value
        water_level_value = self.__greenhouse_data.get_sensor_object(WaterLevelSensor.ID).value
        
        self.model.set_input_values(ph_value = ph_value, water_level_value= water_level_value)
        self.model.defuzzification()
        
        ph_pump_duration = self.__get_ph_pump_value() 
        alkaline_pump_duration = self.__get_alkaline_pump_value() 

        ph_actuator_action = self.__save_action(PHPumpActuator.ID, self.__get_value_of_pump(ph_pump_duration) ,  duration=ph_pump_duration)
        alkaline_actuator_action = self.__save_action(AlkalinePumpActuator.ID,self.__get_value_of_pump(alkaline_pump_duration) , duration=alkaline_pump_duration)

        self.__greenhouse_data.set_actuator_action(ph_actuator_action ,is_automated_action=True)
        self.__greenhouse_data.set_actuator_action(alkaline_actuator_action ,is_automated_action=True)

        return self
    
    def __get_ph_pump_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["ph_pump"]
        raise serializers.ValidationError(detail="Error on PH model defuzzification process")
    
    def __get_alkaline_pump_value(self):
        if self.model.get_ouput_values():
            return self.model.get_ouput_values()["alkaline_pump"]
        raise serializers.ValidationError(detail="Error on PH model defuzzification process")
    
    def __get_value_of_pump(self , duration:float):
        if duration == 0.0:
            return 0
        return 1
        
    
    def __save_action(self, actuator_id:int,value:str,duration:str=None):
        action = ActuatorsAction()
        action.actuator = Actuator.objects.get(pk = actuator_id)
        action.value = value
        action.duration = duration
        action.greenhouse = self.__greenhouse_data.get_greenhouse()
        action.save()
        return action
        
    
    

    