# Generated by Django 4.0.1 on 2022-02-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HardwareApp', '0005_alter_actuator_actuator_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actuator',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]