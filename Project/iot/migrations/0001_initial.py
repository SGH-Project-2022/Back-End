# Generated by Django 4.0.4 on 2022-04-26 09:17

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('action', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='HardwareUploads/')),
            ],
        ),
        migrations.CreateModel(
            name='ActuatorsAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_automated_action', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='PlantsUploads/')),
                ('is_supported', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('password', models.CharField(default='eifmNIU', max_length=10)),
                ('cultivation_type', models.CharField(max_length=120)),
                ('water_tank_size', models.FloatField()),
                ('number_of_crops', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='ProductUploads/')),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token', models.TextField(blank=True, max_length=500, null=True)),
                ('automated_control', models.BooleanField(default=True)),
                ('time_between_automated_action', models.DateTimeField(default='0:10:00')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('messure', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('image', models.ImageField(upload_to='HardwareUploads/')),
            ],
        ),
        migrations.CreateModel(
            name='SensorValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sensor_values', to='iot.product')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.product')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_crops', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.plant')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductActustor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('actuator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.actuator')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='actuators',
            field=models.ManyToManyField(related_name='product_actuators', through='iot.ProductActustor', to='iot.actuator'),
        ),
        migrations.AddField(
            model_name='product',
            name='plants',
            field=models.ManyToManyField(related_name='product_plants', through='iot.ProductPlant', to='iot.plant'),
        ),
        migrations.AddField(
            model_name='product',
            name='sensors',
            field=models.ManyToManyField(related_name='product_sensors', through='iot.ProductSensor', to='iot.sensor'),
        ),
    ]
