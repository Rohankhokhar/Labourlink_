# Generated by Django 5.1.3 on 2025-02-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_complete',
            field=models.BooleanField(default=False),
        ),
    ]
