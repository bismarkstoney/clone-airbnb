# Generated by Django 4.0.5 on 2022-06-19 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_room_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='uploads/rooms'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='amenties',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='houseRules',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.houserule'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.roomtype'),
        ),
    ]
