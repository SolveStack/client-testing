# Generated by Django 3.2.16 on 2022-11-23 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("jive_integration", "0010_alter_jiveline_source_organization_jive_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jivechannel",
            options={"get_latest_by": "modified_at"},
        ),
        migrations.AlterModelOptions(
            name="jiveline",
            options={"get_latest_by": "modified_at"},
        ),
        migrations.AlterModelOptions(
            name="jivesession",
            options={"get_latest_by": "modified_at"},
        ),
        migrations.AddField(
            model_name="jivechannel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="jivechannel",
            name="created_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jivechannel_created",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
        migrations.AddField(
            model_name="jivechannel",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddField(
            model_name="jivechannel",
            name="modified_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jivechannel_modified",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
        migrations.AddField(
            model_name="jiveline",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="jiveline",
            name="created_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jiveline_created",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
        migrations.AddField(
            model_name="jiveline",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddField(
            model_name="jiveline",
            name="modified_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jiveline_modified",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
        migrations.AddField(
            model_name="jivesession",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="jivesession",
            name="created_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jivesession_created",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
        migrations.AddField(
            model_name="jivesession",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AddField(
            model_name="jivesession",
            name="modified_by",
            field=django_userforeignkey.models.fields.UserForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="jivesession_modified",
                to=settings.AUTH_USER_MODEL,
                verbose_name="The user that is automatically assigned",
            ),
        ),
        migrations.AlterField(
            model_name="jiveawsrecordingbucket",
            name="connection",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="bucket",
                to="jive_integration.jiveconnection",
            ),
        ),
    ]
