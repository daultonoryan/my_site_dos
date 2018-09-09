from django.shortcuts import render
from rest_framework import viewsets
from .models import Sensors, Outputs
from .sterilizers import SensorSerializer, OutputSerializer
from django.http import HttpResponse


# Create your views here.

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    serializer_class = SensorSerializer

class OutputViewSet(viewsets.ModelViewSet):
    queryset = Outputs.objects.all()
    serializer_class = OutputSerializer


def change_outputs(request):
    id = request.GET.get("unit_id")
    if not Outputs.objects.filter(unit_id=id).exists():
        Outputs.objects.create(unit_id=request.GET.get("unit_id"), daily_light=request.GET.get("daily_light"),
                               daily_water=request.GET.get("daily_water"), ideal_humidity=request.GET.get("ideal_humidity"),
                               ideal_temp=request.GET.get("ideal_temp")).save()
    else:
        relevant_entry = Outputs.objects.filter(unit_id=id).first()
        relevant_entry.ideal_temp = request.GET.get("ideal_temp")
        relevant_entry.ideal_moisture = request.GET.get("ideal_humidity")
        relevant_entry.daily_light = request.GET.get("daily_light")
        relevant_entry.daily_water = request.GET.get("daily_water")
        relevant_entry.save()
    return HttpResponse("success")
