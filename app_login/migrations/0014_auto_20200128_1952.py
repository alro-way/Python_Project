# Generated by Django 2.2 on 2020-01-29 03:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0013_auto_20200128_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 52, 7, 942401)),
        ),
        migrations.AlterField(
            model_name='features',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feature_created', to='app_login.Users'),
        ),
        migrations.AlterField(
            model_name='features',
            name='proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='app_login.Proposals'),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 52, 7, 938413)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 52, 7, 943405)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_from_instr', to='app_login.Users'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app_login.Proposals'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 52, 7, 943405)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='app_login.Features'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_tasks', to='app_login.Users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 52, 7, 906026)),
        ),
        migrations.AlterField(
            model_name='wireframes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 19, 52, 7, 941407)),
        ),
        migrations.AlterField(
            model_name='wireframes',
            name='proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wireframes', to='app_login.Proposals'),
        ),
    ]
