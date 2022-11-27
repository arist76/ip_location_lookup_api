# Generated by Django 4.1.3 on 2022-11-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ip_lookup", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ipv4model",
            name="version",
            field=models.CharField(default=6, max_length=1),
        ),
        migrations.AlterField(
            model_name="ipv6model",
            name="version",
            field=models.CharField(default=4, max_length=1),
        ),
    ]
