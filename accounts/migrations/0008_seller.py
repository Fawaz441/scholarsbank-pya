# Generated by Django 2.2.6 on 2020-04-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200403_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('whatsapp_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]