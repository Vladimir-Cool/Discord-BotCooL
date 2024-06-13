from django.contrib import admin

from .models import InventoryModel, SlotModel

admin.site.register(InventoryModel)
admin.site.register(SlotModel)
