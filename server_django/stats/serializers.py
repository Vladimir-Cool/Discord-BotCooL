from rest_framework import serializers

from .models import StatsModel


class StatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatsModel
        fields = (
            "id",
            "name",
            "value",
            "description",
        )
        extra_kwargs = {
            "id": {"read_only": True},
        }
