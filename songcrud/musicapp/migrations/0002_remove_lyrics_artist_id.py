# Generated by Django 4.1.2 on 2022-10-27 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lyrics',
            name='artist_id',
        ),
    ]
