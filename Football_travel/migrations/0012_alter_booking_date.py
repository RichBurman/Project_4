# Generated by Django 3.2.20 on 2023-08-04 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Football_travel', '0011_alter_trip_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]