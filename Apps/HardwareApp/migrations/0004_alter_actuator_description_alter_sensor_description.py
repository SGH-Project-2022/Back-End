# Generated by Django 4.0.1 on 2022-02-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HardwareApp', '0003_actuator_image_sensor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='description',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.TextField(max_length=600),
        ),
    ]