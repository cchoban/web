# Generated by Django 2.1 on 2018-10-05 08:23

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20181005_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitpackage',
            name='packageArgs',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='submitpackage',
            name='packageUninstallArgs',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='submitpackage',
            name='server',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
