# Generated by Django 3.1.7 on 2021-03-02 10:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='status',
        ),
        migrations.AddField(
            model_name='hospital',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
