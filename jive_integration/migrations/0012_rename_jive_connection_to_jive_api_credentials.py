# Generated by Django 3.2.16 on 2022-11-23 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0021_auto_20221114_2028'),
        ('jive_integration', '0011_audit_trail_models'),
    ]

    operations = [
        migrations.RenameModel('JiveConnection', 'JiveAPICredentials'),
    ]
