# Generated by Django 4.2.10 on 2024-03-11 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0002_remove_characterstatsmodel_characters_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CharacterStatsModel",
            new_name="StatsModel",
        ),
    ]
