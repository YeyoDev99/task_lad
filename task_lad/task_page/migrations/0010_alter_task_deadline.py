# Generated by Django 4.2.2 on 2023-06-19 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_page', '0009_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 19, 17, 28, 49, 430795, tzinfo=datetime.timezone.utc)),
        ),
    ]