# Generated by Django 4.2.2 on 2023-07-15 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='booking_end_date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='booking_start_date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='is_booked',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_number',
        ),
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('YAC', 'AC ROOM'), ('NAC', 'NON-AC ROOM'), ('DEL', 'DELUXE ROOM'), ('KIN', 'KING ROOM'), ('QUE', 'QUEEN ROOM'), ('STE', 'SUITE ROOM')], max_length=3),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='RoomCategory',
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
