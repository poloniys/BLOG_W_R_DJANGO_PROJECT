# Generated by Django 4.1 on 2022-09-30 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Profile', '0008_mensajes_receiver_mensajes_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
