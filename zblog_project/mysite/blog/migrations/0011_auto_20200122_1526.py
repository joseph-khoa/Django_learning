# Generated by Django 2.2.7 on 2020-01-22 08:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200122_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 22, 8, 26, 41, 546174, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 22, 8, 26, 41, 546174, tzinfo=utc)),
        ),
    ]
