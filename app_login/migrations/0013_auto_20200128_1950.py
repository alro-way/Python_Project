# Generated by Django 2.2 on 2020-01-29 03:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0012_auto_20200128_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 50, 57, 897675)),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 50, 57, 897675)),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proposal_created', to='app_login.Users'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 50, 57, 897675)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 50, 57, 897675)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 50, 57, 850810)),
        ),
        migrations.AlterField(
            model_name='wireframes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 50, 57, 897675)),
        ),
    ]