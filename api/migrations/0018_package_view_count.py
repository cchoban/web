# Generated by Django 2.1 on 2018-08-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
