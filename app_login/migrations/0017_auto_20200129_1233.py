# Generated by Django 2.2 on 2020-01-29 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0016_auto_20200128_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 12, 33, 2, 15284)),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 12, 33, 2, 11289)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 12, 33, 2, 16287)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 12, 33, 2, 16287)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 12, 33, 1, 979336)),
        ),
        migrations.AlterField(
            model_name='wireframes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 12, 33, 2, 14285)),
        ),
    ]