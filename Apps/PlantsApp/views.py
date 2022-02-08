from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Library.permissions import HasGreenhouse
# Create your views here.


class SupportedPlantsView(APIView):
    
    permission_class = [ IsAuthenticated &  HasGreenhouse ]
    def post(self):
        pass

