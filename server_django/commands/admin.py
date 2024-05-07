from django.contrib.admin import ModelAdmin, register
from django.contrib import admin

from commands.models import CommandsModel


@register(CommandsModel)
class CommandsAdmin(ModelAdmin):
    list_display = ["name", "description", "enabled", "embed"]
