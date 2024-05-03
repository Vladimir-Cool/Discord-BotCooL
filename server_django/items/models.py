from django.db import models

from inventory.models import InventoryModel
from characters.models import CharactersModel
from .enums import EQUIPMENT_SLOT_SHOICES


class ItemsModel(models.Model):
    """Модель предметов"""

    name = models.CharField(max_length=256)
    description = models.TextField()

    is_stackable = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)

    RARE_CHOICES = (
        ("C", "common"),
        ("U", "uncommon"),
        ("R", "rarest"),
        ("E", "epic"),
        ("L", "legendary"),
        ("M", "mythic"),
    )
    rarity = models.CharField(max_length=1, choices=RARE_CHOICES, default="C")
    equipment_slot = models.CharField(
        max_length=3, choices=EQUIPMENT_SLOT_SHOICES, default="non"
    )

    # inventory = models.ManyToManyField(
    #     to="inventory.InventoryModel", related_name="items", related_query_name="item"
    # )

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    def __str__(self):
        return f'{self.name}: редкость "{self.rarity}"'


class ItemsInInventoryModel(models.Model):
    """Модель связка предметов с инвенторем персонажа"""

    count = models.IntegerField()
    item = models.ForeignKey(
        to=ItemsModel,
        on_delete=models.CASCADE,
    )
    inventory = models.ForeignKey(
        to=InventoryModel,
        on_delete=models.CASCADE,
        related_name="items",
    )

    class Meta:
        verbose_name = "Предмет в инвентаре"
        verbose_name_plural = "Предметы в инвентаре"


class EquippedItemModel(models.Model):
    """Модель связка предметов с обмундированием персонажа"""

    equipment_slot = models.CharField(
        max_length=3,
        choices=EQUIPMENT_SLOT_SHOICES,
    )

    item = models.ForeignKey(
        to=ItemsModel,
        on_delete=models.CASCADE,
    )
    character = models.ForeignKey(
        to=CharactersModel, on_delete=models.CASCADE, related_name="items"
    )

    class Meta:
        verbose_name = "Экиперованый предмет"
        verbose_name_plural = "Экиперованные предметы"
        unique_together = ("character", "equipment_slot")  # Уникальная связка 2-х полей
