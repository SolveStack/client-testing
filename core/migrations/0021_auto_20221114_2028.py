# Generated by Django 3.2.16 on 2022-11-14 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_auto_20221112_0259"),
    ]

    operations = [
        migrations.AlterField(
            model_name="practice",
            name="organization",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="practices", to="core.organization"),
        ),
        migrations.AlterField(
            model_name="practicetelecom",
            name="voip_provider",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="practice_telecoms", to="core.voipprovider"),
        ),
    ]
