# Generated by Django 3.1.2 on 2021-12-25 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0016_module_module_query_name_without_spaces_all_small'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='module_name',
        ),
        migrations.AlterField(
            model_name='competition',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modulename', to='competitions.module'),
        ),
    ]