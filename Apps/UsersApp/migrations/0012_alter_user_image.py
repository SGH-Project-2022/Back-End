# Generated by Django 4.0.1 on 2022-02-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsersApp', '0011_alter_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='UsersUploads/defaultUserImage.png', upload_to='UsersUploads/'),
        ),
    ]