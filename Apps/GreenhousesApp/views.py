from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Library.permissions import HasGreenhouse
from Apps.GreenhousesApp.models import Greenhouse
from .serializers import GreenhouseSerializers, ConfigureGreenhouseSerializer, GetUserGreenhouseSerializer 
from Library.api_response import ApiResponse
from rest_framework.response import Response
from rest_framework import status

api_response = ApiResponse()


class ConfigureGreenhouseView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):

        api_response.__init__()

        serializer = ConfigureGreenhouseSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors)

        greenhouse = GreenhouseSerializers(serializer.save()).data

        return api_response.set_status_code(status.HTTP_200_OK).set_data("greenhouse", greenhouse).set_data("message",  f"The greenhouse with ID [ {greenhouse.get('id')} ] is configured successfully").response()


class GetUserGreenhousesView(APIView):
    permission_class = [ IsAuthenticated & HasGreenhouse]

    def get(self, request , id = None):
        
        api_response.__init__()

        serializer = GetUserGreenhouseSerializer(data = request.data ,  context={'request':request , 'id':id} )
        
        if not serializer.is_valid():
            return Response(serializer.errors)
        
        greenhouses = GreenhouseSerializers( serializer.save() , many=True ).data
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data("greenhouses", greenhouses).response()
    

class UpdateGreenhouseView(APIView):
    permission_class = [ IsAuthenticated & HasGreenhouse]

    def post(self, request , id):
        api_response.__init__()

        try:
            greenhouse = Greenhouse.objects.get( pk = id, user = self.request.user , is_active = True)
        except Greenhouse.DoesNotExist:
            return api_response.set_status_code(status.HTTP_404_NOT_FOUND).set_data("message", "This greenhouse not found").response()
        
            
        serializer = GreenhouseSerializers(instance = greenhouse ,  data = request.data , context={'request':request , 'id':id} ,  partial=True)
        
        if not serializer.is_valid():
            return api_response.set_status_code(status.HTTP_400_BAD_REQUEST).set_data("errors", serializer.errors).response()
        
        greenhouse = serializer.save()
        
        return api_response.set_status_code(status.HTTP_200_OK).set_data("message","Updated successfully").set_data("greenhouse", serializer.data).response()

