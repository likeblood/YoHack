# Generated by Django 3.0.5 on 2020-04-26 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YoTask', '0003_auto_20200426_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lobby',
            name='roles',
        ),
    ]
