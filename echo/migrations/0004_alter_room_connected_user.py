# Generated by Django 4.1 on 2022-08-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echo', '0003_room_room_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='connected_user',
            field=models.IntegerField(default=1),
        ),
    ]