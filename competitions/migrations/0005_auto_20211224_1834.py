# Generated by Django 3.1.7 on 2021-12-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_auto_20211222_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='event_rules',
            field=models.FileField(blank=True, null=True, storage='rulebooks/', upload_to=''),
        ),
    ]
