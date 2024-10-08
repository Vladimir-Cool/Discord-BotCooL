# Generated by Django 4.2.10 on 2024-03-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0006_equippeditemmodel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemsmodel",
            name="rarity",
            field=models.CharField(
                choices=[
                    ("C", "common"),
                    ("U", "uncommon"),
                    ("R", "rarest"),
                    ("E", "epic"),
                    ("L", "legendary"),
                    ("M", "mythic"),
                ],
                default="C",
                max_length=1,
            ),
        ),
    ]
