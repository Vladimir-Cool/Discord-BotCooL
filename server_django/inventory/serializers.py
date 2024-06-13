from rest_framework import serializers

from .models import InventoryModel, SlotModel


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = ("id", "name", "user", "size", "extra_size")

        extra_kwargs = {
            "id": {"read_only": True},
            "size": {"read_only": True},
            "extra_size": {"read_only": True},
        }


class SlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = SlotModel
        fields = ("id", "inventory", "content", "count")

        extra_kwargs = {
            "id": {"read_only": True},
            "count": {"read_only": True},
            "contenr": {"read_only": True},
        }

class InventoryFullSerializer(InventorySerializer):
    slots = SlotSerializer(read_only=True, many=True)

    class Meta:
        model = InventoryModel
        fields = ("id", "name", "user", "slots", "size", "extra_size")
