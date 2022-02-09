# Generated by Django 4.0.1 on 2022-02-04 12:20

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0007_alter_user_image_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=255),
        ),
    ]