# Generated by Django 4.2.10 on 2024-03-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0005_alter_charactersmodel_id"),
        ("items", "0009_alter_equippeditemmodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equippeditemmodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="itemsininventorymodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="itemsmodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="equippeditemmodel",
            unique_together={("character", "equipment_slot")},
        ),
    ]
