# Generated by Django 4.1 on 2022-09-30 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP_Profile', '0011_alter_mensajes_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='usuario',
        ),
    ]
