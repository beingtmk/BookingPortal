# Generated by Django 2.0.4 on 2018-04-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingportal', '0002_auto_20180416_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='roll_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
