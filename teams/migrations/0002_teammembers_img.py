# Generated by Django 3.1.2 on 2021-12-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammembers',
            name='img',
            field=models.ImageField(default='user-default.png', upload_to='image_uploads/userdp/'),
        ),
    ]
