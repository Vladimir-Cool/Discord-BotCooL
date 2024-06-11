from django.db import models


class InventoryModel(models.Model):
    name = models.CharField(max_length=150, default="Удалить")
    size = models.IntegerField(default=8, null=False, blank=False)
    extra_size = models.IntegerField(default=0, null=False, blank=False)

    user = models.OneToOneField(
        to="user.User", on_delete=models.CASCADE, related_name="inventory"
    )

    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural = "Инвентари"

    def __str__(self):
        return self.name

    # Ранее инвентарь был на персонаже.
    # character = models.OneToOneField(
    #     to="characters.CharactersModel",
    #     on_delete=models.CASCADE,
    #     related_name="inventory",
    # )
