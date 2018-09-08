from django.shortcuts import render
from rest_framework import viewsets, request
from .models import Sensors, Outputs
from .sterilizers import SensorSerializer, OutputSerializer


# Create your views here.

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorSerializer

class OoutputViewSet(viewsets.ModelViewSet):
    queryset = Outputs.objects.all()
    serializer_class = OutputSerializer