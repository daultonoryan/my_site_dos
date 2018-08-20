from rest_framework import serializers
from .models import Sensors


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensors
        fields = ["temp", "unit_id", "humidity", "soil_moisture", "light_status"]