# Generated by Django 4.2.5 on 2023-10-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolingapp', '0015_rename_design_cooling_coolingforecast_approach_temperature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coolingforecast',
            name='cooling_machine_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
