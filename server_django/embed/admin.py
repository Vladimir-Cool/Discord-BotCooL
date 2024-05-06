from django.contrib.admin import ModelAdmin, register, site
from django.db import models

from .models import EmbedModel

# site.register(EmbedModel)
@register(EmbedModel)
class EmbedAdmin(ModelAdmin):
    list_display = ("name", "embed_template", "embed_enabled")


    # formfield_overrides = {
    #     models.TextField: {'widget': Code()},
    # }
