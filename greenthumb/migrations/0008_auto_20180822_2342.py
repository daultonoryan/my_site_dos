# Generated by Django 2.1 on 2018-08-22 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenthumb', '0007_auto_20180822_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensors',
            name='snapshot',
            field=models.ImageField(blank=True, upload_to='statc/snapshots'),
        ),
    ]
