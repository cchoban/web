# Generated by Django 2.1 on 2018-10-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20180910_0328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submitpackage',
            name='package',
        ),
        migrations.AddField(
            model_name='submitpackage',
            name='packageIcon',
            field=models.ImageField(default='noimage.png', upload_to='media/'),
        ),
    ]