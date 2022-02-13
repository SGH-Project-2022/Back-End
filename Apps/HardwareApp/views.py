from itsdangerous import Serializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Library.permissions import HasGreenhouse
from .serializers import SensorValuesSerializer

# Input

# id	value	greenhouse_id	sensor_id

class SensorsValuesView(APIView):
    # permission_classes = [HasGreenhouse & IsAuthenticated]
    def post(self , request):
        serializer = SensorValuesSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        
        return Response(True)



class TakeAcionView(APIView):
    # permission_classes = [HasGreenhouse & IsAuthenticated]
    def post(self , request):
        pass




