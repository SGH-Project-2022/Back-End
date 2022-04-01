import socketio
from Library.api_response import ApiResponse
from rest_framework import status
from Apps.Hardware.serializers.requests_serializers import TakeActionSerializer 
from Apps.Hardware.serializers.models_serializers import  ActuatorActionsSerializer
from Library.api_response import ApiResponse
from rest_framework import status
from SocketIO.socketio_server_settings import HARDWARE_NAMESPACE, WEB_NAMESPACE, MOBILE_NAMESPACE
from Apps.Hardware.requests import take_action


#------------------------------------------------------ Frontend Client
class WebNamespace(socketio.Namespace):
    
    def on_connect(self, sid, environ):
        print("Web Connected Successfully")
        api_response = ApiResponse()
        response = api_response.set_status_code(200).set_data('message','Connected to server successfully').get()
        self.enter_room(sid, 'myGreenhouse' , namespace=WEB_NAMESPACE)
        self.emit('connection_status', response , room="myGreenhouse" , namespace=WEB_NAMESPACE)
        
    def on_take_action(self,sid,data):
        

        response = take_action(data)
        
        self.emit('take_action', response  ,room='myGreenhouse', namespace=HARDWARE_NAMESPACE)


        self.emit('action_taked', response, namespace=WEB_NAMESPACE,  room='myGreenhouse')        
        self.emit('action_taked', response  ,room='myGreenhouse', namespace=MOBILE_NAMESPACE)

    
    def on_disconnect(self, sid):
        print("Web Disconnected")
    



