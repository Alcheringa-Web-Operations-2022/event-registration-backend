# Generated by Django 3.1.2 on 2021-12-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20211230_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=20),
        ),
    ]
