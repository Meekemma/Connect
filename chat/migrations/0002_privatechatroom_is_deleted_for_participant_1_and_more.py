# Generated by Django 5.2.3 on 2025-07-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatechatroom',
            name='is_deleted_for_participant_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='privatechatroom',
            name='is_deleted_for_participant_2',
            field=models.BooleanField(default=False),
        ),
    ]
