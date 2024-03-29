# Generated by Django 3.2.16 on 2022-11-23 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0021_auto_20221114_2028"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("jive_integration", "0012_rename_jive_connection_to_jive_api_credentials"),
    ]

    operations = [
        migrations.AddField(
            model_name="jiveapicredentials",
            name="access_token",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="jiveapicredentials",
            name="access_token_expires_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="jiveapicredentials",
            name="created_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jiveapicredentials_created",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
        migrations.AlterField(
            model_name="jiveapicredentials",
            name="modified_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jiveapicredentials_modified",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
    ]
