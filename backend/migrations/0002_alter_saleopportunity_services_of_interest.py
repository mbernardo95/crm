# Generated by Django 4.2.4 on 2023-08-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saleopportunity",
            name="services_of_interest",
            field=models.ManyToManyField(blank=True, to="backend.service"),
        ),
    ]