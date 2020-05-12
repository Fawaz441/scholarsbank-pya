# Generated by Django 2.2.6 on 2020-04-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarswork', '0015_products_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Phones and Accessories', 'PAA'), ('Clothing', 'WC'), ('Computers and Accessories', 'CAA'), ('Food Items', 'Food items')], max_length=50),
        ),
    ]
