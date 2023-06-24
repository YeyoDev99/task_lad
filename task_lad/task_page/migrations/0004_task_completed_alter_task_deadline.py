# Generated by Django 4.2.2 on 2023-06-18 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_page', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 18, 13, 58, 41, 358189)),
        ),
    ]