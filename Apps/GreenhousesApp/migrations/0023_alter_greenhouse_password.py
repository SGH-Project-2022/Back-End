# Generated by Django 4.0.1 on 2022-02-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreenhousesApp', '0022_alter_greenhouse_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenhouse',
            name='password',
            field=models.CharField(default='UntQxAK', max_length=10),
        ),
    ]
