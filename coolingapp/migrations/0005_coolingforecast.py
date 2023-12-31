# Generated by Django 4.2.5 on 2023-10-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolingapp', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoolingForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InletTemp', models.FloatField()),
                ('OutletTemp', models.FloatField()),
                ('OutdoorWetBulb', models.FloatField()),
                ('OutdoorAirTemp', models.FloatField()),
                ('OutdoorAirHumidity', models.FloatField()),
                ('Kw_cooling', models.FloatField()),
                ('Kw_Chiller', models.FloatField()),
                ('Design_cooling', models.FloatField()),
                ('Diff_Outlet_Wetbulb', models.FloatField()),
                ('Status', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
