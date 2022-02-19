# Generated by Django 4.0.1 on 2022-02-19 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hardware', '0001_initial'),
        ('Plants', '0001_initial'),
        ('Greenhouses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='greenhousesensor',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.sensor'),
        ),
        migrations.AddField(
            model_name='greenhouseplant',
            name='greenhouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Greenhouses.greenhouse'),
        ),
        migrations.AddField(
            model_name='greenhouseplant',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plants.plant'),
        ),
        migrations.AddField(
            model_name='greenhouseactustor',
            name='actuator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hardware.actuator'),
        ),
        migrations.AddField(
            model_name='greenhouseactustor',
            name='greenhouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Greenhouses.greenhouse'),
        ),
        migrations.AddField(
            model_name='greenhouse',
            name='actuators',
            field=models.ManyToManyField(related_name='greenhouse_actuators', through='Greenhouses.GreenhouseActustor', to='Hardware.Actuator'),
        ),
        migrations.AddField(
            model_name='greenhouse',
            name='plants',
            field=models.ManyToManyField(related_name='greenhouse_plants', through='Greenhouses.GreenhousePlant', to='Plants.Plant'),
        ),
        migrations.AddField(
            model_name='greenhouse',
            name='sensors',
            field=models.ManyToManyField(related_name='greenhouse_sensors', through='Greenhouses.GreenhouseSensor', to='Hardware.Sensor'),
        ),
    ]
