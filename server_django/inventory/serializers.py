from rest_framework import serializers

from .models import InventoryModel


class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = ("characters",)
