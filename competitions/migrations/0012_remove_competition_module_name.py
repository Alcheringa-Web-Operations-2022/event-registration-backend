# Generated by Django 3.1.2 on 2021-12-25 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0011_auto_20211225_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='module_name',
        ),
    ]
