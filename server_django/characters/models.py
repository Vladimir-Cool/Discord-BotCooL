from django.db import models


class CharactersModel(models.Model):
    """
    Модель игрового персонажа
    stats - обратная связь к модели CharacterStatsModel
    inventory - Обратная связь к модели InventoryModel
    # race
    # quest
    """

    name = models.CharField(max_length=40, unique=True)
    level = models.IntegerField(default=1, blank=True)
    experience = models.IntegerField(default=0, blank=True)

    user = models.ForeignKey(
        to="user.User",
        on_delete=models.CASCADE,
        related_name="characters",
    )

    class Meta:
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self):
        return f"{self.name}"
