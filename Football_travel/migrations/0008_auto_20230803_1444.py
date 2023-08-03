# Generated by Django 3.2.20 on 2023-08-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Football_travel', '0007_alter_trip_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='seats_required',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='trip',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='trip',
            name='remaining_seats',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='trip',
            name='seats',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
