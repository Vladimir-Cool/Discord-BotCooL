from django.db import models

from embed.models import EmbedModel

class CommandsModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    enabled = models.BooleanField()

    embed_message = models.ForeignKey(to=EmbedModel, on_delete=models.CASCADE)



    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self):
        return self.name
