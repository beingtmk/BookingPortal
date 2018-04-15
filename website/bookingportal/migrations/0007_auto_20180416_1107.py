# Generated by Django 2.0.4 on 2018-04-16 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingportal', '0006_auto_20180416_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='roll_number',
            field=models.IntegerField(blank=True, default='slot1', null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='slot',
            field=models.CharField(choices=[('slot1', '1'), ('slot2', '2')], max_length=10),
        ),
    ]
