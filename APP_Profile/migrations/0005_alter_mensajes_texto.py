# Generated by Django 4.1 on 2022-09-30 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Profile', '0004_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='texto',
            field=models.TextField(default=datetime.datetime(2018, 7, 7, 9, 11, 6, 489063)),
            preserve_default=False,
        ),
    ]
