# Generated by Django 3.1.2 on 2021-12-22 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0002_auto_20211216_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compteam',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_name1', to='competitions.competition'),
        ),
        migrations.AlterField(
            model_name='compteam',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_leader', to='authentication.newuser'),
        ),
        migrations.CreateModel(
            name='PreviousPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('link', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_name2', to='competitions.competition')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compteams2', to='competitions.compteam')),
            ],
        ),
    ]