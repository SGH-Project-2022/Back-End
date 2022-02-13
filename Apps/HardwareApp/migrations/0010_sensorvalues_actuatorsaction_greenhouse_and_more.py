# Generated by Django 4.0.1 on 2022-02-11 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GreenhousesApp', '0026_alter_greenhouse_password'),
        ('HardwareApp', '0009_rename_messure_actuator_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GreenhousesApp.greenhouse')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HardwareApp.sensor')),
            ],
        ),
        migrations.AddField(
            model_name='actuatorsaction',
            name='greenhouse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='GreenhousesApp.greenhouse'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SensorValue',
        ),
    ]