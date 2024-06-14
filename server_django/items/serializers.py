from rest_framework import serializers

from .models import ItemsModel
from .enums import EQUIPMENT_SLOT_SHOICES, RARE_CHOICES


class ItemsSerializer(serializers.ModelSerializer):
    rarity = serializers.ChoiceField(choices=RARE_CHOICES)
    equipment_slot = serializers.ChoiceField(choices=EQUIPMENT_SLOT_SHOICES)

    class Meta:
        model = ItemsModel
        fields = (
            "id",
            "name",
            "rarity",
            "description",
            "equipment_slot",
            "is_stackable",
            "is_used",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            # "is_stackable": {"read_only": True},
            # "is_used": {"read_only": True},
        }

class ItemsSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsModel
        fields = (
            "name",
            "description",

        )
        extra_kwargs = {
            "name": {"read_only": True},
            "description": {"read_only": True},
        }