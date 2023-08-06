# Generated by Django 3.2.20 on 2023-08-06 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Football_travel', '0013_alter_trip_remaining_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='remaining_seats',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(80)]),
        ),
    ]
