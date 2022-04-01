from Apps.Greenhouses.greenhouse_data_model import GreenhouseDataModel
from Apps.Hardware.serializers.models_serializers import ActuatorActionsSerializer
from .models_implementations.ph_model_implementation import PHModelImplementation
from .models_implementations.temperature_model_implementation import TemperatureModelImplementation
from Library.api_response import ApiResponse
from rest_framework import status
from SocketIO.socketio_server_settings import HARDWARE_NAMESPACE, WEB_NAMESPACE, MOBILE_NAMESPACE

CONTROLLERS = [
    PHModelImplementation(),
    # TemperatureModelImplementation()
]

def implement(greenhouse_data:GreenhouseDataModel):
    actions = []
    for controller in CONTROLLERS:
        controller.set_greenhouse_data_model(greenhouse_data)
        if not controller.validation():
            continue 
        actions +=controller.make_actions().get_greenhouse_data_model().get_automated_actions()
    return actions
    

def take_fuzzy_actions(socket , actions:list):
    for action in actions:
        api_response = ApiResponse()
        api_response.set_status_code(status.HTTP_200_OK)
        print(action)
        action_reponse = api_response.set_data("action",ActuatorActionsSerializer(action).data).get()
        socket.emit('take_action', action_reponse, namespace=HARDWARE_NAMESPACE,  room='myGreenhouse')
        socket.emit('action_taked', action_reponse, namespace=MOBILE_NAMESPACE,  room='myGreenhouse')
        socket.emit('action_taked', action_reponse, namespace=WEB_NAMESPACE,  room='myGreenhouse')
