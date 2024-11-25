# Generated by Django 5.1.3 on 2024-11-23 11:52

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='price',
            new_name='mrp',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='description',
        ),
        migrations.AddField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2025, 11, 23, 11, 52, 16, 471458, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='medicine',
            name='mfg_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='medicine',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]