# Generated by Django 3.2.15 on 2022-09-26 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jive_integration", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jivecallpartial",
            old_name="external_id",
            new_name="source_jive_id",
        ),
        migrations.RenameField(
            model_name="jivechannel",
            old_name="external_id",
            new_name="source_jive_id",
        ),
    ]