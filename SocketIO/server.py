import os
import socketio
from Library.api_response import ApiResponse
from rest_framework import status
from Apps.Hardware.serializers import SensorValueSerializer , SensorSerializer , ActuatorSerializer , StoreSensorValuesSerializer
from Apps.Greenhouses.serializers import GreenhouseSerializers , GreenhouseAuthSerializer
from Library.api_response import ApiResponse


basedir = os.path.dirname(os.path.realpath(__file__))

sio = socketio.Server(async_mode=None  ,cors_allowed_origins = '*' , logger=True, engineio_logger=True)

thread = None   


    
#------------------------------------------------------ Hardware Client
class HardwareNamespace(socketio.Namespace):
    
    def on_connect(self, sid, message):

        print("BAdr")
        # serializer = GreenhouseAuthSerializer(data = message )
        
        # if serializer.is_valid():
        #     raise ConnectionRefusedError('authentication failed')
        
        # greenhouse , token = serializer.login()
        
        clients_response = ApiResponse()
        hardware_response = ApiResponse()
        
        response = clients_response.set_status_code(200).set_data('message','Hardware connected successfully').get()

        sio.enter_room(sid , namespace='/' ,  room="myGreenhouse")
        self.emit('connection_status', hardware_response.set_data('token',"token").get()  , namespace='/', room="myGreenhouse")
        self.emit('hardware_connection', response  , namespace='/web' ,  room="myGreenhouse")
        self.emit('hardware_connection', response ,  namespace='/mobile' , room="myGreenhouse")
        # sio.enter_room(sid, str(1) , namespace='/')
        # self.emit('connection_status', hardware_response.set_data('token',"token").get()  , namespace='/', room=str(1))
        # self.emit('hardware_connection', response  , namespace='/web' ,  room=str(1))
        # self.emit('hardware_connection', response ,  namespace='/mobile' ,  room=str(1))
        # sio.enter_room(sid, str(greenhouse.id) , namespace='/hardware')
        # self.emit('connection_status', hardware_response.set_data('token',token).get()  , namespace='/hardware' , room=str(greenhouse.id))
        # self.emit('hardware_connection', response  , namespace='/web' ,  room=str(greenhouse.id))
        # self.emit('hardware_connection', response ,  namespace='/mobile' ,  room=str(greenhouse.id))

    def on_sensors_values(self , sid , message):
        api_response = ApiResponse()
        print(
            'hello'
        )
        serializer = StoreSensorValuesSerializer(data = message)
        
        if not serializer.is_valid():
            response = api_response.set_data("errors" , serializer.errors)
        else:
            sensor_values = serializer.save()
            greenhouse = serializer.get_greenhouse()
            api_response.set_status_code(status.HTTP_200_OK).set_data("greenhouse",GreenhouseSerializers(greenhouse).data).set_data("sensors",SensorValueSerializer(sensor_values,many=True).data)

        response = api_response.get()
            
        self.emit('sensors_values', response  , namespace='/web'  ,  room='myGreenhouse' )
        self.emit('sensors_values', response ,  namespace='/mobile' ,  room='myGreenhouse')


    def on_disconnect(self, sid):
        api_response = ApiResponse()
        response = api_response.set_status_code(400).set_data('message','Hardware disconnected').get()
        self.emit('hardware_connection', response  , namespace='/web' ,  room='myGreenhouse')
        self.emit('hardware_connection', response ,  namespace='/mobile' ,  room='myGreenhouse')
    
# sio.register_namespace(HardwareNamespace('/socket.io/hardware&transport=polling'))
sio.register_namespace(HardwareNamespace('/'))




#------------------------------------------------------ Frontend Client
class WebNamespace(socketio.Namespace):
    
    def on_connect(self, sid, environ):
        sio.enter_room(sid, 'myGreenhouse' , namespace="/web")
        api_response = ApiResponse()
        response = api_response.set_status_code(200).set_data('message','Connected to server successfully').get()
        sio.emit('connection_status', response , room=sid , namespace='/web')
        
    def on_take_action(self,sid,data):
        api_response = ApiResponse()
        response = api_response.set_status_code(200).set_data('message','Please take action').get()
        self.emit('take_action', response  , namespace='/hardware')

    
    def on_disconnect(self, sid):
        pass
    
sio.register_namespace(WebNamespace('/web'))


    
    
#------------------------------------------------------ Mobile Client
class MobileNamespace(socketio.Namespace):
    def on_connect(self, sid, environ):
        api_response = ApiResponse()
        response = api_response.set_status_code(200).set_data('message','Connected to server successfully').get()
        sio.emit('connection_status', response , room=sid , namespace='/mobile')

    def on_take_action(self,sid,data):
        api_response = ApiResponse()
        response = api_response.set_status_code(200).set_data('message','Please take action').get()
        self.emit('take_action', response  , namespace='/hardware')
        
    def on_disconnect(self, sid):
        pass

sio.register_namespace(MobileNamespace('/mobile'))




































# The environ argument is a dictionary in standard WSGI format containing the request information, including HTTP headers.
# The auth argument contains any authentication details passed by the client, or None if the client did not pass anything. 
# After inspecting the request, the connect event handler can return False to reject the connection with the client.
#  raise socketio.exceptions.ConnectionRefusedError('authentication failed')






