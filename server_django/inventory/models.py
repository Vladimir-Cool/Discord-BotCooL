from django.db import models


class InventoryModel(models.Model):

    characters = models.OneToOneField(
        to="characters.CharactersModel",
        on_delete=models.CASCADE,
        related_name="inventory",
    )

    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural = "Инвентари"
