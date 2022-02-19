# Generated by Django 4.0.1 on 2022-02-19 17:40

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greenhouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('password', models.CharField(default='JGMZHIH', max_length=10)),
                ('cultivation_type', models.CharField(max_length=120)),
                ('water_tank_size', models.FloatField()),
                ('number_of_crops', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='GreenhouseUploads/')),
                ('frame_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GreenhouseActustor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GreenhousePlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_crops', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GreenhouseSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Greenhouses.greenhouse')),
            ],
        ),
    ]