from rest_framework import serializers

from .models import InventoryModel


class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = ("id", "name", "user", "size", "extra_size")

        extra_kwargs = {
            "id": {"read_only": True},
            "size": {"read_only": True},
            "extra_size": {"read_only": True},
        }
