# Generated by Django 2.0.5 on 2018-07-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_usersetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersetting',
            name='token_reset_day',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
