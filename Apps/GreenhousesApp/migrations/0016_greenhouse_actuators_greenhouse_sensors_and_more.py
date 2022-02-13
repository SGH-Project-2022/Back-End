# Generated by Django 4.0.1 on 2022-02-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HardwareApp', '0001_initial'),
        ('GreenhousesApp', '0015_alter_greenhouse_password_alter_greenhouse_plants'),
    ]

    operations = [
        migrations.AddField(
            model_name='greenhouse',
            name='actuators',
            field=models.ManyToManyField(related_name='greenhouse_actuators', to='HardwareApp.Actuators'),
        ),
        migrations.AddField(
            model_name='greenhouse',
            name='sensors',
            field=models.ManyToManyField(related_name='greenhouse_sensros', to='HardwareApp.Sensors'),
        ),
        migrations.AlterField(
            model_name='greenhouse',
            name='password',
            field=models.CharField(default='BfPz2yB', max_length=10),
        ),
    ]
