# Generated by Django 3.2.20 on 2023-08-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Football_travel', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seats_required',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2),
        ),
    ]
