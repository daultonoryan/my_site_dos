# Generated by Django 2.0.5 on 2018-07-08 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20180601_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=400)),
                ('url', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
