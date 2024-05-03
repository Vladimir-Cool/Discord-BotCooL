from django.contrib import admin

from .models import StatsModel, CharacterStatsModel, ItemStatsModel

admin.site.register(StatsModel)
admin.site.register(CharacterStatsModel)
admin.site.register(ItemStatsModel)
