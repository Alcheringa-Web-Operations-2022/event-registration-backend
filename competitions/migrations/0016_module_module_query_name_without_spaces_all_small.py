# Generated by Django 3.1.2 on 2021-12-25 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0015_auto_20211225_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='module_query_name_without_spaces_all_small',
            field=models.CharField(default=django.utils.timezone.now, max_length=127),
            preserve_default=False,
        ),
    ]
