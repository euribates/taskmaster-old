# Generated by Django 3.1.1 on 2020-10-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_task_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='closed',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]