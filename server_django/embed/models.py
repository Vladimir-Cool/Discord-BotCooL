from django.db import models


class EmbedModel(models.Model):

    name = models.CharField(max_length=255, unique=True)
    embed_template = models.TextField()
    embed_enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Embed"
        verbose_name_plural = "Embeds"

    def __str__(self):
        return self.name
