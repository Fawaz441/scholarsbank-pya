# Generated by Django 2.2.6 on 2020-04-03 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scholarswork', '0005_auto_20200403_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefiles',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 15, 13, 9, 968251, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 15, 13, 9, 968251, tzinfo=utc)),
        ),
    ]