# Generated by Django 3.2.16 on 2022-11-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "jive_integration",
            "0009_remove_unique_and_add_bucket_name_and_add_choices_to_events",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="jiveline",
            name="source_organization_jive_id",
            field=models.CharField(max_length=64),
        ),
    ]
