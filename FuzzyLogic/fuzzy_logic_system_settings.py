from datetime import timedelta
from Apps.Hardware.hardware_library.sensors import TempratureSensor , PHSensor , WaterLevelSensor
from Apps.Hardware.hardware_library.actuators import FanActuator , AlkalinePumpActuator , PHPumpActuator
from .models.ph_model import PHFuzzyLogic
from .models.temperature_model import TempFuzzyLogic
from .models_implementations.ph_model_implementation import PHModelImplementation
from .models_implementations.temperature_model_implementation import TemperatureModelImplementation

TIME_BETWEEN_FUZZY_ACTIONS = timedelta(minutes=0)

ALLOW_AUTOMATED_CONTROL = True

CONTROLLERS = [
    {
        "sensors": [TempratureSensor.ID],
        "model":TempFuzzyLogic(),
        "model_implemetation":PHModelImplementation(),
        "actuators":[
            FanActuator.ID
        ]
    },
    {
        "sensors": [PHSensor.ID, WaterLevelSensor.ID],
        "model":PHFuzzyLogic(),
        "model_implemetation":TemperatureModelImplementation(),
        "actuators":[ 
            PHPumpActuator.ID,
            AlkalinePumpActuator.ID
        ]
    }
]