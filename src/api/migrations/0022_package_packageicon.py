# Generated by Django 2.1 on 2018-10-05 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20181005_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='packageIcon',
            field=models.ImageField(default='noimage.png', upload_to='media/'),
        ),
    ]