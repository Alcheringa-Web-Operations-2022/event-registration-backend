# Generated by Django 3.1.2 on 2021-12-29 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0020_module_module_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compteam',
            name='teamname',
        ),
    ]