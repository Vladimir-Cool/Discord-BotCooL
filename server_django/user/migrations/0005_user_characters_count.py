# Generated by Django 4.2.10 on 2024-03-11 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_user_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="characters_count",
            field=models.IntegerField(default=0),
        ),
    ]
