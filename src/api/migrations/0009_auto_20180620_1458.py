# Generated by Django 2.0.6 on 2018-06-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180617_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_update_packages', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='do_update',
        ),
    ]
