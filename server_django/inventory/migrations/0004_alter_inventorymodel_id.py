# Generated by Django 4.2.10 on 2024-03-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_alter_inventorymodel_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventorymodel",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
