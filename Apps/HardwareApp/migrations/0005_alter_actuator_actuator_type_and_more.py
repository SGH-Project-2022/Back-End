# Generated by Django 4.0.1 on 2022-02-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HardwareApp', '0004_alter_actuator_description_alter_sensor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='actuator_type',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
