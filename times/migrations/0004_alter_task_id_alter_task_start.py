# Generated by Django 5.0.4 on 2024-05-22 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0003_alter_task_id_alter_task_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 22, 12, 44, 50, 116057)),
        ),
    ]
