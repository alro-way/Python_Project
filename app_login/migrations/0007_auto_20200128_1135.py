# Generated by Django 2.2 on 2020-01-28 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0006_auto_20200128_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 11, 35, 7, 660337)),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 11, 35, 7, 656345)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 11, 35, 7, 660337)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 11, 35, 7, 660337)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 11, 35, 7, 616184)),
        ),
        migrations.AlterField(
            model_name='wireframes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 11, 35, 7, 659337)),
        ),
    ]
