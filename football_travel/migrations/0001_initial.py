# Generated by Django 3.2.20 on 2023-08-09 14:09

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_name', models.CharField(max_length=50)),
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('seats', models.IntegerField(default=80)),
                ('remaining_seats', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(80)])),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True)),
                ('seats_required', models.IntegerField()),
                ('total_cost', models.IntegerField(default=0)),
                ('trip_booked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='football_travel.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
