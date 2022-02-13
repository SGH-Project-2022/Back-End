from xml.etree.ElementInclude import include
from django.urls import path , include
from . import views

urlpatterns = [
    # path('sgh/socket', views.index, name="index"),
    path('hardware', include([
        path('',views.SensorsValuesView.as_view()),    
    ])),
    
]


#/sgh/socket/hardware