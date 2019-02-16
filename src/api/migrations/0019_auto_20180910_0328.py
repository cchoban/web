# Generated by Django 2.1 on 2018-09-10 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_package_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='showcase',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='package',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Category'),
        ),
    ]