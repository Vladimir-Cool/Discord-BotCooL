# Generated by Django 4.2.10 on 2024-05-07 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("embed", "0001_initial"),
        ("commands", "0004_rename_embed_name_commandsmodel_embed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commandsmodel",
            name="embed",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="embed.embedmodel",
            ),
        ),
    ]
