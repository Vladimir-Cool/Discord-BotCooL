from django.contrib import admin

from .models import ItemsModel, ItemsInInventoryModel, EquippedItemModel

admin.site.register(ItemsModel)
admin.site.register(ItemsInInventoryModel)
admin.site.register(EquippedItemModel)
