# Generated by Django 3.0.2 on 2020-01-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0002_auto_20200126_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.IntegerField(),
        ),
    ]
