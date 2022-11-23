# Generated by Django 3.2.15 on 2022-09-10 01:28

import localflavor.us.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_alter_insuranceprovider_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="practice",
            name="address_us_state",
            field=localflavor.us.models.USStateField(blank=True, default="AZ", max_length=2),
        ),
    ]