# Generated by Django 2.2.6 on 2020-04-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarswork', '0014_auto_20200408_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default='this shoe is soooo cool', max_length=1000),
            preserve_default=False,
        ),
    ]
