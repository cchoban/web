# Generated by Django 2.0.6 on 2018-06-11 15:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180610_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='packageName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='submitpackage',
            name='packageArgs',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='submitpackage',
            name='packageUninstallArgs',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='submitpackage',
            name='server',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
