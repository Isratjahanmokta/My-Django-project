# Generated by Django 4.1.3 on 2022-11-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0004_userprofile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
