# Generated by Django 5.1.3 on 2024-11-23 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_alter_medicine_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(default=datetime.datetime(2025, 11, 23, 16, 44, 36, 575129, tzinfo=datetime.timezone.utc)),
        ),
    ]
