# Generated by Django 4.2.14 on 2024-08-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trainer", "0005_alter_trainer_managers_remove_trainer_last_login"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainer",
            name="is_subscribed",
            field=models.BooleanField(default=False, verbose_name="구독 유무"),
        ),
    ]
