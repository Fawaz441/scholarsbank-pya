# Generated by Django 2.2.6 on 2020-04-03 15:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scholarswork', '0007_auto_20200403_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefiles',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 15, 14, 7, 77690, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
