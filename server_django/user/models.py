from django.db import models
from django.utils.timezone import now


class User(models.Model):
    """
    Модель пользователя
    characters - обратная связь с модели UserSerializer
    """

    discord_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    experience = models.IntegerField(default=0, blank=True)

    characters_count = models.IntegerField(default=2)  # Количество персанажей

    last_activity_time = models.DateTimeField(default=now)
    registration_date = models.DateTimeField(default=now)

    # inventory = models.OneToOneField(
    #     to="inventory.InventoryModel", on_delete=models.CASCADE, related_name="user"
    # )

    # roles = models.ManyToManyField()
    # active_roles = models.ForeignKey()

    # speciality = models.ManyToManyField()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.name} {int(self.experience / 100)} уровень ({self.experience % 100}%)"
