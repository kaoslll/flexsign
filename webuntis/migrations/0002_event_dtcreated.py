# Generated by Django 2.1.2 on 2018-10-16 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webuntis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dtcreated',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 16, 20, 44, 0, 396395, tzinfo=utc)),
        ),
    ]