# Generated by Django 4.1 on 2022-09-30 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP_Profile', '0010_alter_mensajes_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
