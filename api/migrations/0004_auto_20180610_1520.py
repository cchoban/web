# Generated by Django 2.0.6 on 2018-06-10 13:20

import api.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_submitpackage_waitingforapprovalpackages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WaitingForApprovalPackages',
        ),
        migrations.AddField(
            model_name='submitpackage',
            name='packageArgs',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}'),
        ),
        migrations.AddField(
            model_name='submitpackage',
            name='packageName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='submitpackage',
            name='packageUninstallArgs',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}'),
        ),
        migrations.AddField(
            model_name='submitpackage',
            name='server',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}'),
        ),
        migrations.AlterField(
            model_name='submitpackage',
            name='package',
            field=models.FileField(upload_to='uploads/', validators=[api.validators.validate_file_extension]),
        ),
    ]