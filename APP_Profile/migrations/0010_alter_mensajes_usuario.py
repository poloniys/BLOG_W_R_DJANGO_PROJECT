# Generated by Django 4.1 on 2022-09-30 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP_Profile', '0009_mensajes_sent_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
