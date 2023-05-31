# Generated by Django 3.2.12 on 2023-05-31 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_taskstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duedate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todo',
            name='taskstatus',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('WORKING', 'WORKING'), ('DONE', 'DONE'), ('OVERDUE', 'OVERDUE')], default='OPEN', max_length=20),
        ),
    ]