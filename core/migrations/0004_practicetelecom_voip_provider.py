# Generated by Django 3.2.11 on 2022-01-25 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_voipprovider'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicetelecom',
            name='voip_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.voipprovider'),
        ),
    ]
