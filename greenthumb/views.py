from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensors
from .sterilizers import SensorSerializer

# Create your views here.

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorSerializer



