# Generated by Django 4.2.2 on 2023-07-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='First Name', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=30),
        ),
    ]