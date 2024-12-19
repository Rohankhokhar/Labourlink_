# Generated by Django 5.1.3 on 2024-12-19 04:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0002_remove_partiesdetail_id_partiesdetail_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partiesdetail',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partiesdetail',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
