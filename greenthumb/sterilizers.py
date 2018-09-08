from rest_framework import serializers
from .models import Sensors, Outputs


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensors
        fields = ["temp", "unit_id", "humidity", "soil_moisture", "light_status"]


class OutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outputs
        fields = ["unit_id", "ideal_temp", "ideal_water", "daily_water", "daily_light"]