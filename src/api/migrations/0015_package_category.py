# Generated by Django 2.0.5 on 2018-08-06 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20180806_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
    ]
