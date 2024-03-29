# Generated by Django 3.2.16 on 2022-11-04 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("jive_integration", "0004_delete_jivecallpartial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jivesubscriptioneventextract",
            name="jive_channel",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="jive_integration.jivechannel",
            ),
        ),
        migrations.AlterField(
            model_name="jiveconnection",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="jiveconnection",
            name="last_sync",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="jivesubscriptioneventextract",
            name="data_created",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="jivesubscriptioneventextract",
            name="data_originator_id",
            field=models.CharField(db_index=True, max_length=36),
        ),
        migrations.AlterField(
            model_name="jivesubscriptioneventextract",
            name="data_originator_organization_id",
            field=models.CharField(db_index=True, max_length=36),
        ),
        migrations.AlterField(
            model_name="jivesubscriptioneventextract",
            name="data_state",
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name="jivesubscriptioneventextract",
            name="entity_id",
            field=models.CharField(max_length=128),
        ),
    ]
