# Generated by Django 2.0.5 on 2020-01-12 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20200112_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='principla',
            new_name='principal',
        ),
    ]
