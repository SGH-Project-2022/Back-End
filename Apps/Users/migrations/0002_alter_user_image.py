# Generated by Django 4.0.3 on 2022-03-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='UsersUploads/defaultUserImage.png', null=True, upload_to='UsersUploads/'),
        ),
    ]
