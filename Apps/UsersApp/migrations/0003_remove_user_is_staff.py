# Generated by Django 4.0.1 on 2022-01-30 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0002_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
