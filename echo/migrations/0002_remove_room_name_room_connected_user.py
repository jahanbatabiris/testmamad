# Generated by Django 4.1 on 2022-08-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
        migrations.AddField(
            model_name='room',
            name='connected_user',
            field=models.IntegerField(default=0),
        ),
    ]
