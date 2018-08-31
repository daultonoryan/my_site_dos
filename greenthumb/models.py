from django.db import models

# Create your models here.
class Sensors (models.Model):
    unit_id = models.CharField(max_length=200, default="10101010101101")
    temp = models.IntegerField(default=20)
    humidity = models.IntegerField(default=24)
    soil_moisture = models.IntegerField(default=200)
    water_tank = models.IntegerField(default=1)
    light_status = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, blank=True)
