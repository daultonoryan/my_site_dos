# Generated by Django 2.1 on 2018-08-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenthumb', '0011_sensors_water_tank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='water_tank',
            field=models.IntegerField(default=1),
        ),
    ]
