# Generated by Django 2.0.5 on 2018-07-29 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_package_download_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
