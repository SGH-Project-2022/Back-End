# Generated by Django 4.0.1 on 2022-02-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='PlantsUploads/')),
            ],
        ),
    ]
