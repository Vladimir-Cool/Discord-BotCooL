from django.db import models

from characters.models import CharactersModel
from items.models import ItemsModel


class StatsModel(models.Model):
    """Модель параметров персонажа"""

    name = models.CharField(max_length=50)
    value = models.IntegerField()
    description = models.TextField(default=None, null=True)
    # characters = models.OneToOneField(
    #     to="characters.CharactersModel", on_delete=models.CASCADE, related_name="stats"
    # )

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.name


class CharacterStatsModel(models.Model):
    count = models.IntegerField()

    stat = models.ForeignKey(
        to=StatsModel,
        on_delete=models.CASCADE,
    )
    character = models.ForeignKey(
        to=CharactersModel,
        on_delete=models.CASCADE,
        related_name="stats",
    )

    class Meta:
        verbose_name = "Характеристика персонажа"
        verbose_name_plural = "Характеристики персонажей"
        unique_together = ("character", "stat")  # Уникальная связка 2-х полей

    def __str__(self):
        character = CharactersModel.objects.get(
            pk=self.character.id
        )  # type CharacterModel
        stat = StatsModel.objects.get(pk=self.stat.id)  # type StatsModel
        return f'"{character.name}" имеет {self.count} {stat.name}'


class ItemStatsModel(models.Model):
    count = models.IntegerField()

    stat = models.ForeignKey(
        to=StatsModel,
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        to=ItemsModel,
        on_delete=models.CASCADE,
        related_name="stats",
    )

    class Meta:
        verbose_name = "Характеристика предмета"
        verbose_name_plural = "Характеристики предметов"
        unique_together = ("item", "stat")  # Уникальная связка 2-х полей

    def __str__(self):
        item = ItemsModel.objects.get(pk=self.item.id)  # type ItemsModel
        stat = StatsModel.objects.get(pk=self.stat.id)  # type StatsModel
        return f'"{item.name}" имеет {self.count} {stat.name}'
