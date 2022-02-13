import os
import socketio
from Library.api_response import ApiResponse

api_response = ApiResponse()

def rest_api_response():
    api_response.__init__()

basedir = os.path.dirname(os.path.realpath(__file__))

sio = socketio.Server(async_mode=None , cors_allowed_origins = '*' , logger=True, engineio_logger=True)

thread = None   


    
#------------------------------------------------------ Hardware Client
class HardwareNamespace(socketio.Namespace):
    
    def on_connect(self, sid, environ):
        rest_api_response()
        response = api_response.set_status_code(200).set_data('message','Hardware connected to server successfully').get()
        self.emit('connection_status', response , room=sid , namespace='/hardware')
        self.emit('hardware_connection', response  , namespace='/web')
        self.emit('hardware_connection', response ,  namespace='/mobile')

    def on_sensors_values(self , sid , message):
        rest_api_response()
        response = api_response.set_status_code(200).set_data('message','sensor values').get()
        self.emit('sensors_values', response  , namespace='/web')
        self.emit('sensors_values', response ,  namespace='/mobile')

    def on_disconnect(self, sid):
        rest_api_response()
        response = api_response.set_status_code(400).set_data('message','Hardware disconnected').get()
        self.emit('hardware_connection', response  , namespace='/web')
        self.emit('hardware_connection', response ,  namespace='/mobile')
    
sio.register_namespace(HardwareNamespace('/hardware'))




#------------------------------------------------------ Frontend Client
class WebNamespace(socketio.Namespace):
    
    def on_connect(self, sid, environ):
        rest_api_response()
        response = api_response.set_status_code(200).set_data('message','Connected to server successfully').get()
        sio.emit('connection_status', response , room=sid , namespace='/web')
        
    def on_take_action(self,sid,data):
        rest_api_response()
        response = api_response.set_status_code(200).set_data('message','Please take action').get()
        self.emit('take_action', response  , namespace='/hardware')

    
    def on_disconnect(self, sid):
        pass
    
sio.register_namespace(WebNamespace('/web'))


    
    
#------------------------------------------------------ Mobile Client
class MobileNamespace(socketio.Namespace):
    def on_connect(self, sid, environ):
        rest_api_response()
        response = api_response.set_status_code(200).set_data('message','Connected to server successfully').get()
        sio.emit('connection_status', response , room=sid , namespace='/mobile')

    def on_take_action(self,sid,data):
        rest_api_response()
        response = api_response.set_status_code(200).set_data('message','Please take action').get()
        self.emit('take_action', response  , namespace='/hardware')
        
    def on_disconnect(self, sid):
        pass

sio.register_namespace(MobileNamespace('/mobile'))




































# The environ argument is a dictionary in standard WSGI format containing the request information, including HTTP headers.
# The auth argument contains any authentication details passed by the client, or None if the client did not pass anything. 
# After inspecting the request, the connect event handler can return False to reject the connection with the client.
#  raise socketio.exceptions.ConnectionRefusedError('authentication failed')








































# import os
# import socketio
# from Library.api_response import ApiResponse


# basedir = os.path.dirname(os.path.realpath(__file__))
# sio = socketio.Server(async_mode=None , cors_allowed_origins = '*' , logger=True, engineio_logger=True)
# thread = None   


# api_response = ApiResponse()
# def rest_api_response():
#     api_response.__init__()
    

# # # Clients 
# # HARDWARE   = 1 
# # WEB_FRONTEND = 2 
# # MOBILE_APP   = 3 

# # def get_client(requset):
# #     if "client" in requset.keys:

# #------------------------------------------------------ Events
# class SGHNamespace(socketio.Namespace):
    
#     def on_connect(self, sid, environ):
#         rest_api_response()
#         response = api_response.set_status_code(200).set_data('message','Hardware connected to server successfully').get()
#         self.emit('connection_status', response , room=sid , namespace='/hardware')
#         self.emit('hardware_connection', response  , namespace='/web')
#         self.emit('hardware_connection', response ,  namespace='/mobile')

#     def on_sensors_values(self , sid , message):
#         rest_api_response()
#         response = api_response.set_status_code(200).set_data('message','sensor values').get()
#         self.emit('sensors_values', response  , namespace='/web')
#         self.emit('sensors_values', response ,  namespace='/mobile')

#     def on_disconnect(self, sid):
#         rest_api_response()
#         response = api_response.set_status_code(400).set_data('message','Hardware disconnected').get()
#         self.emit('hardware_connection', response  , namespace='/web')
#         self.emit('hardware_connection', response ,  namespace='/mobile')
    
# sio.register_namespace(SGHNamespace('/sgh'))

