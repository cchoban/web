# Generated by Django 2.0.5 on 2018-07-29 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_usersetting_token_reset_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersetting',
            name='token_reset_day',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
