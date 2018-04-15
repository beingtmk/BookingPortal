# Generated by Django 2.0.4 on 2018-04-16 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slot', models.CharField(max_length=10)),
                ('roll_number', models.IntegerField(blank=True)),
                ('ca', models.CharField(blank=True, max_length=50)),
                ('approvedby_ca', models.NullBooleanField(default=False)),
                ('approvedby_chairman', models.NullBooleanField(default=False)),
                ('is_booked', models.BooleanField(default=False)),
                ('comments_ca', models.CharField(blank=True, max_length=500)),
                ('comments_chairman', models.CharField(blank=True, max_length=500)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
