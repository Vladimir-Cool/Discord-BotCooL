# Generated by Django 4.2.10 on 2024-03-11 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0010_alter_equippeditemmodel_id_and_more"),
        ("characters", "0005_alter_charactersmodel_id"),
        ("stats", "0005_alter_statsmodel_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statsmodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.CreateModel(
            name="ItemStatsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField()),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="items.itemsmodel",
                    ),
                ),
                (
                    "stat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stats.statsmodel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CharacterStatsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField()),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="characters.charactersmodel",
                    ),
                ),
                (
                    "stat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stats.statsmodel",
                    ),
                ),
            ],
        ),
    ]
