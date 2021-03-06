# Generated by Django 3.0.2 on 2020-01-26 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(max_length=100),
        ),
    ]
