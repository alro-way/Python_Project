# Generated by Django 2.2 on 2020-01-28 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0008_auto_20200128_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 12, 24, 47, 105049)),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 12, 24, 47, 101021)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 12, 24, 47, 106043)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 12, 24, 47, 107041)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 12, 24, 47, 69833)),
        ),
        migrations.AlterField(
            model_name='wireframes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 12, 24, 47, 105049)),
        ),
    ]
