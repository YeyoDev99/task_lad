# Generated by Django 4.2.2 on 2023-06-18 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_page', '0004_task_completed_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True)),
        ),
    ]